
data "archive_file" "lambdas" {
  type        = "zip"
  source_dir  = "lambdas"
  output_path = "lambdas.zip"
}

resource "aws_lambda_function" "lambda_copy_image" {
  filename         = "lambdas.zip"
  function_name    = "tf-copy-image"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "copy_image.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
}

resource "aws_lambda_function" "lambda_get_copy_status" {
  filename         = "lambdas.zip"
  function_name    = "tf-get-copy-status"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "get_copy_status.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
}

resource "aws_lambda_function" "lambda_split_image" {
  filename         = "lambdas.zip"
  function_name    = "tf-split-image"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "split_image.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
}

resource "aws_lambda_function" "lambda_image_cleanup" {
  filename         = "lambdas.zip"
  function_name    = "tf-image-cleanup"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "image_cleanup.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
}
