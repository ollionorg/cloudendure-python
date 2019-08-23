
data "archive_file" "lambdas" {
  type        = "zip"
  source_dir  = "lambdas"
  output_path = "lambdas.zip"
}

resource "aws_lambda_function" "lambda_find_instance" {
  filename         = "lambdas.zip"
  function_name    = "tf-find-instance"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "find_instance.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
}

resource "aws_lambda_function" "lambda_get_instance_status" {
  filename         = "lambdas.zip"
  function_name    = "tf-get-instance-status"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "get_instance_status.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
}

resource "aws_lambda_function" "lambda_create_image" {
  filename         = "lambdas.zip"
  function_name    = "tf-create-image"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "create_image.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
}

resource "aws_lambda_function" "lambda_get_image_status" {
  filename         = "lambdas.zip"
  function_name    = "tf-get-image-status"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "get_image_status.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
}

resource "aws_lambda_function" "lambda_share_image" {
  filename         = "lambdas.zip"
  function_name    = "tf-share-image"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "share_image.lambda_handler"
  source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
  runtime          = "python3.7"
  depends_on       = ["data.archive_file.lambdas"]
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

// resource "aws_lambda_function" "lambda_image_cleanup" {
//   filename         = "lambdas.zip"
//   function_name    = "tf-image-cleanup"
//   role             = "${aws_iam_role.iam_for_lambda.arn}"
//   handler          = "image_cleanup.lambda_handler"
//   source_code_hash = "${data.archive_file.lambdas.output_base64sha256}"
//   runtime          = "python3.7"
//   depends_on       = ["data.archive_file.lambdas"]
// }
