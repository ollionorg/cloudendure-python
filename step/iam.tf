# state function related iam
resource "aws_iam_role" "iam_for_statefunction" {
  name = "tf-iam-for-stepfunction"

  assume_role_policy = "${data.aws_iam_policy_document.statefunction_assume_role_policy_document.json}"
}

data "aws_iam_policy_document" "statefunction_assume_role_policy_document" {
  statement {
    actions = [
      "sts:AssumeRole"
    ]

    principals {
      type = "Service"
      identifiers = [
        "states.ap-southeast-1.amazonaws.com",
        "events.amazonaws.com"
      ]
    }
  }
}
