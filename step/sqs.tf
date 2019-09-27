resource "aws_sqs_queue" "event_queue" {
  name                      = "cloudendure-migration-queue"
  delay_seconds             = 10
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10
  redrive_policy            = "{\"deadLetterTargetArn\":\"${aws_sqs_queue.dead_letter_queue.arn}\",\"maxReceiveCount\":4}"
}

resource "aws_sqs_queue" "dead_letter_queue" {
  name                      = "cloudendure-dead-letter-queue"
}