// resource "aws_cloudwatch_log_group" "cloudendure-rehost-migration-log-group" {
//   name              = "/aws/lambda/cloudendure-rehost-migration"
//   retention_in_days = "1"
// }

resource "aws_cloudwatch_event_rule" "rehost_migration_rule" {
  name          = "ce-rehost-migration-rule"
  description   = ""
  event_pattern = <<PATTERN
{
  "source": [
    "aws.ec2"
  ],
  "detail-type": [
    "EC2 Instance State-change Notification"
  ],
  "detail": {
    "state": [
      "running"
    ]
  }
}
PATTERN
}

resource "aws_cloudwatch_event_target" "rehost_migration_target" {
  rule     = "${aws_cloudwatch_event_rule.rehost_migration_rule.id}"
  arn      = "${aws_sfn_state_machine.rehost_migration.id}"
  role_arn = "${aws_iam_role.iam_for_cloudwatch_stepfunction.arn}"
}

resource "aws_lambda_event_source_mapping" "event_source_mapping" {
  event_source_arn = "${aws_sqs_queue.event_queue.arn}"
  function_name    = "${aws_lambda_function.lambda_update_status.arn}"
  batch_size       = 1
}