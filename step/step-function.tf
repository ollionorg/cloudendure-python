resource "aws_sfn_state_machine" "copy_and_split" {
  name     = "tf-copy-and_split"
  role_arn = "${aws_iam_role.iam_for_stepfunction.arn}"

  definition = <<EOF
{
  "Comment": "A state machine that copies a usually shared image and splits it into a root AMI tagged with its snapshots and attachment information",
  "StartAt": "Copy Image",
  "States": {
    "Copy Image": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_copy_image.arn}",
      "ResultPath": "$.copy_ami",
      "Next": "Wait X Seconds",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Wait X Seconds": {
      "Type": "Wait",
      "SecondsPath": "$.wait_time",
      "Next": "Get Copy Status"
    },
    "Get Copy Status": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_get_copy_status.arn}",
      "ResultPath": "$.status",
      "Next": "Copy Complete?",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Copy Complete?": {
      "Type": "Choice",
      "Choices": [
        {
          "Or": [
            {
            "Variable": "$.status",
            "StringEquals": "failed"
            },
            {
            "Variable": "$.status",
            "StringEquals": "error"
            }
          ],
          "Next": "Job Failed"
        },
        {
          "Variable": "$.status",
          "StringEquals": "available",
          "Next": "Split Image"
        }
      ],
      "Default": "Wait X Seconds"
    },
    "Job Failed": {
      "Type": "Fail",
      "Cause": "Copy Failed",
      "Error": "Copy Image returned failed or error."
    },
    "Split Image": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_split_image.arn}",
      "ResultPath": "$.split_ami_id",
      "End": true,
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    }
  }
}
  EOF
}
