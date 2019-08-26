# -*- coding: utf-8 -*-
"""Define the CloudEndure template logic."""
from __future__ import annotations


class TerraformTemplate:
    """Define Terraform template entries.

    Attributes:
        INSTANCE_TEMPLATE (str): The Terraform EC2 instance template.
        NETWORKTEMPLATE (str): The Terraform network interface template.
        VOLUME_TEMPLATE (str): The Terraform volume and volume attachment template.

    """

    INSTANCE_TEMPLATE: str = """
resource "aws_instance" "ec2_instance_{name}" {{
  ami                  = "{image_id}"
  instance_type        = "${{var.instance_type}}"
  key_name             = "{keypair}"
  iam_instance_profile = "${{local.iam_instance_profile}}"
  tags                 = "${{merge(module.{tagging_module}.tags, map("Name", "{uppercase_name}"))}}"

  network_interface {{
    network_interface_id = "${{aws_network_interface.eni_primary_{name}.id}}"
    device_index         = 0
  }}

  root_block_device {{
    volume_type = "gp2"
    volume_size = "100"
  }}

  tags = {{
    Name        = "{uppercase_name}"
  }}

  lifecycle {{
    ignore_changes = ["ami"]
  }}
}}
"""

    NETWORK_TEMPLATE: str = """
resource "aws_network_interface" "eni_primary_{name}" {{
  subnet_id       = "{subnet_id}"
  private_ips     = ["{private_ip}"]
  security_groups = ["${{aws_security_group.{security_group}.id}}"]
  tags            = "${{merge(module.{tagging_module}.tags, map("Name", "ap-eni-{name}-sg"))}}"
}}
"""

    VOLUME_TEMPLATE: str = """
resource "aws_ebs_volume" "datadisk_{name}_{drive_name}" {{
  availability_zone = "{region}a"
  type              = "{volume_type}"
  size              = {volume_size}
  encrypted         = true
  snapshot_id       = "{snapshot_id}"
  tags             = "${{merge(module.{tagging_module}.tags, map("Name", "ap-vol-{name}-{drive_name}-sg"))}}"
}}

resource "aws_volume_attachment" "ebs_att_disk_{name}_{drive_name}" {{
  device_name = "{drive}"
  volume_id   = "${{aws_ebs_volume.datadisk_{name}_{drive_name}.id}}"
  instance_id = "${{aws_instance.ec2_instance_{name}.id}}"
}}
"""
