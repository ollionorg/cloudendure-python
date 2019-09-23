# step function related iam
resource "aws_iam_role" "iam_for_stepfunction" {
  name               = "ce-iam-for-stepfunction"
  assume_role_policy = "${data.aws_iam_policy_document.stepfunction_assume_role_policy_document.json}"
}

data "aws_iam_policy_document" "stepfunction_assume_role_policy_document" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type = "Service"
      identifiers = ["states.${var.region}.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "lambda-invoke" {
  statement {
    actions = [
      "lambda:InvokeFunction"
    ]
    resources = [
      "*",
    ]
  }
  # role(s) that the lambdas are allowed to assume roles on for copy, split, and tf generation
  statement {
    effect = "Allow"
    actions = [ "sts:AssumeRole" ]
    resources = [for role in var.assume_role_list: role]
  }
}

resource "aws_iam_policy" "lambda-invoke" {
  name   = "ce-lambda-invoke"
  policy = "${data.aws_iam_policy_document.lambda-invoke.json}"
}

resource "aws_iam_role_policy_attachment" "lambda-invoke" {
  role       = "${aws_iam_role.iam_for_stepfunction.name}"
  policy_arn = "${aws_iam_policy.lambda-invoke.arn}"
}

# lambda related
resource "aws_iam_role" "iam_for_lambda" {
  name               = "ce-iam-for-lambda"
  assume_role_policy = "${data.aws_iam_policy_document.iam_for_lambda_assume_role.json}"
}

data "aws_iam_policy_document" "iam_for_lambda_assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "role_policy_lambda_exec" {
  role       = "${aws_iam_role.iam_for_lambda.name}"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "role_policy_lambda_ec2" {
  role       = "${aws_iam_role.iam_for_lambda.name}"
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
}
 