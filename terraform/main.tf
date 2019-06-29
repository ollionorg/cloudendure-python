data "aws_iam_policy_document" "cloudendure_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "this" {
  name               = "cloudendure-access-role"
  assume_role_policy = "${data.aws_iam_policy_document.cloudendure_role_policy.json}"
}

data "aws_iam_policy_document" "cloudendure" {
  statement {
    sid = "Enable IAM User Permissions"

    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::${var.source_account_number}:root"]
    }

    actions   = ["kms:*"]
    resources = ["*"]
  }

  statement {
    sid = "Allow access for Key Administrators"

    principals {
      type = "AWS"
      identifiers = ["arn:aws:iam::${var.source_account_number}:role/cloudendure-access-role"]
    }

    actions = [
      "kms:Create*",
      "kms:Describe*",
      "kms:Enable*",
      "kms:List*",
      "kms:Put*",
      "kms:Update*",
      "kms:Revoke*",
      "kms:Disable*",
      "kms:Get*",
      "kms:Delete*",
      "kms:TagResource",
      "kms:UntagResource",
      "kms:ScheduleKeyDeletion",
      "kms:CancelKeyDeletion",
    ]

    resources = [
      "*",
    ]
  }

  statement {
    sid = "Allow use of the key"

    principals {
      type = "AWS"
      identifiers = [
        "arn:aws:iam::${var.destination_account_number}:role/${var.destination_role_name}",
        "arn:aws:iam::${var.source_account_number}:user/CloudEndureAccess",
      ]
    }

    actions = [
      "kms:CreateGrant",
      "kms:Encrypt",
      "kms:Decrypt",
      "kms:ReEncrypt*",
      "kms:GenerateDataKey*",
      "kms:DescribeKey",
    ]

    resources = [
      "*",
    ]
  }
}

resource "aws_iam_role_policy" "this" {
  name   = "cloudendure_access_role_policy"
  role   = "${aws_iam_role.this.id}"
  policy = "${data.aws_iam_policy_document.cloudendure.json}"
}
