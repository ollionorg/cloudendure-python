# -*- coding: utf-8 -*-
"""Define the CloudEndure template logic."""
from __future__ import annotations

from typing import Any, Dict

from cookiecutter.main import cookiecutter


class CookiecutterHandler:
    """Handle cookiecutter operations."""

    def run(
        self,
        migration_data: Dict[str, Any],
        cookiecutter_path: str = "https://github.com/2ndWatch/cookiecutter-tf-cloudendure",
    ) -> None:
        """Run the automation of cookiecutter."""
        print("Running cookiecutter project creation with package: ", cookiecutter_path)
        for k, v in migration_data.items():
            print("Creating the cookiecutter repository subdirectory for: ", k)
            self.create_project(package_path=cookiecutter_path, context=v)

    def create_project(
        self, package_path: str, context: Dict[Any, Any] = None, no_input: bool = True
    ) -> bool:
        """Create a cookiecutter project with the provided details.

        Args:
            package_path (str): The path to the cookiecutter template.
            context (dict): The seed context to be used to populate cookiecutter values.
                Defaults to an empty dictionary.
            no_input (bool): Whether or not the interaction is no input.
                Requires True in order to function for bulk creation.
                Defaults to: True.

        Returns:
            bool: Whether or not project creation was successful.

        """
        if not context:
            context = {}

        try:
            cookiecutter(package_path, no_input=no_input, extra_context=context)
        except Exception as e:
            print("Exception: (%s) encountered in create_project", e)
            return False
        return True


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
