variable "region" {
  default     = "us-east-1"
  description = "The AWS region to be used."
  type        = string
}

variable "assume_role_list" {
  default = []
  description = ""
  type = list(string)
}
