
resource "aws_sfn_state_machine" "image_and_share" {
  name     = "tf-image-and-share"
  role_arn = "${aws_iam_role.iam_for_stepfunction.arn}"

  definition = <<EOF
{
  "Comment": "A state machine that finds for a converted CloudEndure instance, waits for it to become viable, creates an image, and shares it to a destination account",
  "StartAt": "Find Instance",
  "States": {
    "Find Instance": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_find_instance.arn}",
      "ResultPath": "$.instance_id",
      "Next": "Instance Found?",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Instance Found?": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.instance_id",
          "StringEquals": "not-found",
          "Next": "Wait For Instance"
        },
        {
          "Variable": "$.instance_id",
          "StringEquals": "timed-out",
          "Next": "Image Failed"
        }
      ],
      "Default": "Get Instance Status"
    },
    "Wait For Instance": {
      "Type": "Wait",
      "Seconds": 300,
      "Next": "Find Instance"
    },
    "Get Instance Status": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_get_instance_status.arn}",
      "ResultPath": "$.instance_status",
      "Next": "Instance Ready?",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Instance Ready?": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.instance_status",
          "StringEquals": "running",
          "Next": "Create Image"
        },
        {
          "Or": [
            {
            "Variable": "$.instance_status",
            "StringEquals": "stopped"
            },
            {
            "Variable": "$.instance_status",
            "StringEquals": "terminated"
            }
          ],
          "Next": "Image Failed"
        }
      ],
      "Default": "Wait 10 Minutes"
    },
    "Wait 10 Minutes": {
      "Type": "Wait",
      "Seconds": 600,
      "Next": "Get Instance Status"
    },
    "Create Image": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_create_image.arn}",
      "ResultPath": "$.migrated_ami_id",
      "Next": "Get Image Status",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Get Image Status": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_get_image_status.arn}",
      "ResultPath": "$.ami_status",
      "Next": "Image Complete?",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Image Complete?": {
      "Type": "Choice",
      "Choices": [
        {
          "Or": [
            {
            "Variable": "$.ami_status",
            "StringEquals": "failed"
            },
            {
            "Variable": "$.ami_status",
            "StringEquals": "error"
            }
          ],
          "Next": "Image Failed"
        },
        {
          "Variable": "$.ami_status",
          "StringEquals": "available",
          "Next": "Share Image"
        }
      ],
      "Default": "Wait 5 Minutes"
    },
    "Wait 5 Minutes": {
      "Type": "Wait",
      "Seconds": 300,
      "Next": "Get Image Status"
    },
    "Image Failed": {
      "Type": "Fail",
      "Cause": "Image Failed",
      "Error": "Create Image returned failed or error."
    },
    "Share Image": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_share_image.arn}",
      "ResultPath": "$.shared",
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
          "Next": "Copy Failed"
        },
        {
          "Variable": "$.status",
          "StringEquals": "available",
          "Next": "Split Image"
        }
      ],
      "Default": "Wait X Seconds"
    },
    "Copy Failed": {
      "Type": "Fail",
      "Cause": "Copy Failed",
      "Error": "Copy Image returned failed or error."
    },
    "Split Image": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_split_image.arn}",
      "ResultPath": "$.split_ami_id",
      "Next": "Image Cleanup",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Image Cleanup": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_image_cleanup.arn}",
      "ResultPath": "$.cleanup",
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
