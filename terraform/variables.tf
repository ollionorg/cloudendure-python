variable "source_account_number" {
  description = "The source AWS account where the CloudEndure generated image resides."
  type        = "string"
}

variable "destination_account_numbers" {
  default     = []
  description = "The destination AWS account where images will be copied."
  type        = "list"
}
