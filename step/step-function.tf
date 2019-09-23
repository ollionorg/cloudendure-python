resource "aws_sfn_state_machine" "rehost_migration" {
  name       = "ce-rehost-migration"  
  role_arn   = "${aws_iam_role.iam_for_stepfunction.arn}"

  definition = <<EOF
{
  "Comment": "A state machine that finds for a converted CloudEndure instance, waits for it to become viable, creates an image, and shares it to a destination account",
  "StartAt": "Find Instance",
  "States": {
    "Find Instance": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_find_instance.arn}",
      "ResultPath": "$",
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
          "Next": "Not A Migration Instance"
        },
        {
          "Variable": "$.instance_id",
          "StringEquals": "not-migration",
          "Next": "Not A Migration Instance"
        }
      ],
      "Default": "Get Instance Status"
    },
    "Not A Migration Instance": {
      "Type": "Succeed"
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
      "Default": "Wait For Instance"
    },
    "Wait For Instance": {
      "Type": "Wait",
      "Seconds": 60,
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
      "Default": "Wait For Image"
    },
    "Wait For Image": {
      "Type": "Wait",
      "Seconds": 60,
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
      "Next": "Copy Image",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Copy Image": {
      "Type": "Task",
      "Resource": "${aws_lambda_function.lambda_copy_image.arn}",
      "ResultPath": "$.copy_ami",
      "Next": "Wait For Copy",
      "Retry": [
        {
          "ErrorEquals": ["States.ALL"],
          "IntervalSeconds": 1,
          "MaxAttempts": 3,
          "BackoffRate": 2
        }
      ]
    },
    "Wait For Copy": {
      "Type": "Wait",
      "Seconds": 60,
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
      "Default": "Wait For Copy"
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
      "ResultPath": "$.cleaned_up",
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
