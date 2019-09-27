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
      identifiers = [
        "states.${var.region}.amazonaws.com"
      ]
    }
  }
}

data "aws_iam_policy_document" "lambda_invoke" {
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

resource "aws_iam_policy" "lambda_invoke" {
  name   = "ce-lambda-invoke"
  policy = "${data.aws_iam_policy_document.lambda_invoke.json}"
}

resource "aws_iam_role_policy_attachment" "lambda-invoke" {
  role       = "${aws_iam_role.iam_for_stepfunction.name}"
  policy_arn = "${aws_iam_policy.lambda_invoke.arn}"
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

resource "aws_iam_role_policy_attachment" "role_policy_lambda_sqs" {
  role       = "${aws_iam_role.iam_for_lambda.name}"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaSQSQueueExecutionRole"
}

resource "aws_iam_role_policy_attachment" "role_policy_lambda_ec2" {
  role       = "${aws_iam_role.iam_for_lambda.name}"
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2FullAccess"
}

resource "aws_iam_policy" "role_policy_sqs" {
  name   = "ce-lambda-sqs"
  policy = "${data.aws_iam_policy_document.role_policy_sqs_document.json}"
}

data "aws_iam_policy_document" "role_policy_sqs_document" {
  statement {
    effect = "Allow"
    actions = [
      "sqs:SendMessage",
      "sqs:GetQueueUrl"
    ]
    resources = [
      "${aws_sqs_queue.event_queue.arn}"
    ]
  }
}

resource "aws_iam_role_policy_attachment" "role_policy_sqs_attachment" {
  role       = "${aws_iam_role.iam_for_lambda.name}"
  policy_arn = "${aws_iam_policy.role_policy_sqs.arn}"
}

// CW event execution

resource "aws_iam_role" "iam_for_cloudwatch_stepfunction" {
  name               = "ce-cloudwatch-stepfunction"
  assume_role_policy = "${data.aws_iam_policy_document.stepfunction_assume_role_document.json}"
}

data "aws_iam_policy_document" "stepfunction_assume_role_document" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type = "Service"
      identifiers = ["events.amazonaws.com"]
    }
  }
}

resource "aws_iam_policy" "stepfunction_execution" {
  name   = "ce-cloudwatch-stepfunction"
  policy = "${data.aws_iam_policy_document.stepfunction_execution_policy_document.json}"
}

data "aws_iam_policy_document" "stepfunction_execution_policy_document" {
  statement {
    effect = "Allow"
    actions = ["states:StartExecution"]
    resources = ["${aws_sfn_state_machine.rehost_migration.id}"]
  }
}

resource "aws_iam_role_policy_attachment" "stepfunction_execution_attachment" {
  role       = "${aws_iam_role.iam_for_cloudwatch_stepfunction.name}"
  policy_arn = "${aws_iam_policy.stepfunction_execution.arn}"
}