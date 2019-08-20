resource "aws_cloudwatch_log_group" "copy-and-split-log-group" {
  name              = "/aws/lambda/copy-and-split"
  retention_in_days = "1"
}
