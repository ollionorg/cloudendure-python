// resource "aws_cloudwatch_log_group" "cloudendure-rehost-migration-log-group" {
//   name              = "/aws/lambda/cloudendure-rehost-migration"
//   retention_in_days = "1"
// }

resource "aws_cloudwatch_event_rule" "rehost-migration-rule" {
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

resource "aws_cloudwatch_event_target" "rehost-migration-target" {
  rule     = "${aws_cloudwatch_event_rule.rehost-migration-rule.id}"
  arn      = "${aws_sfn_state_machine.rehost_migration.id}"
  role_arn = "${aws_iam_role.iam_for_stepfunction.arn}"
}