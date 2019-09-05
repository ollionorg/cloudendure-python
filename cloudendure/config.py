# -*- coding: utf-8 -*-
"""Define the CloudEndure Config related logic."""
from __future__ import annotations

import logging
import os
from pathlib import Path, PosixPath
from typing import Any, Dict, List

import yaml

logger: logging.Logger = logging.getLogger(__name__)
LOG_LEVEL: str = os.environ.get("CLOUDENDURE_LOG_LEVEL", "INFO")
logger.setLevel(getattr(logging, LOG_LEVEL))


class CloudEndureConfig:
    """Define the CloudEndure Config object."""

    BASE_CONFIG = {
        "host": "https://console.cloudendure.com",
        "api_version": "latest",
        "auth_ttl": "3600",
        "username": "",
        "password": "",
        "token": "",
        "user_api_token": "",
        "session_cookie": "",
        "project_name": "",
        "project_id": "",
        "max_lag_ttl": "90",
        "machines": "",
        "migration_wave": "0",
        "clone_status": "NOT_STARTED",
        "destination_account": "",
        "destination_kms": "",
        "destination_role": "",
        "disk_type": "SSD",
        "public_ip": "DONT_ALLOCATE",
    }

    def __init__(
        self, username: str = "", password: str = "", token: str = "", *args, **kwargs
    ) -> None:
        """Initialize the Environment."""
        logger.info("Initializing the CloudEndure Configuration")
        _config_path: str = os.environ.get(
            "CLOUDENDURE_CONFIG_PATH", "~/.cloudendure.yaml"
        )
        if _config_path.startswith("~"):
            self.config_path = os.path.expanduser(_config_path)

        # Handle CloudEndure CLI input credentials.
        self.cli = {"username": username, "password": password, "user_api_token": token}

        _config: PosixPath = Path(self.config_path)
        if not _config.exists():
            print(
                "No CloudEndure YAML configuration found! Creating it at: (%s)",
                self.config_path,
            )
            self.write_yaml_config(config=self.BASE_CONFIG)
        self.update_config()

    def __str__(self) -> str:
        """Define the string representation of the CloudEndure API object."""
        return "<CloudEndureAPI>"

    def merge_config_dicts(self, values: List[Any]) -> Dict[str, str]:
        """Merge a list of configuration dictionaries."""
        data: Dict[str, str] = self.BASE_CONFIG
        for value in values:
            data.update({k: v for k, v in value.items() if v})
        return data

    def read_yaml_config(self) -> Dict[str, Any]:
        """Read the CloudEndure YAML configuration file."""
        logger.info("Loading the CloudEndure YAML configuration file")
        with open(self.config_path, "r") as yaml_stream:
            try:
                config: Dict[str, Any] = yaml.safe_load(yaml_stream)
            except yaml.YAMLError as e:
                logger.error("YAMLError during read_yaml_config: %s", str(e))
                config = {}
        return config

    def write_yaml_config(self, config: Dict[str, Any]) -> bool:
        """Write to the CloudEndure YAML configuration file."""
        logger.info("Writing to the CloudEndure YAML configuration file")
        with open(self.config_path, "w") as yaml_file:
            try:
                yaml.dump(config, yaml_file, default_flow_style=False)
                logger.info("CloudEndure YAML configuration saved!")
                return True
            except Exception as e:
                logger.error(
                    "Exception encountered while writing the CloudEndure YAML configuration file - (%s)",
                    e,
                )
        return False

    def update_yaml_config(self, kwargs: Dict[str, Any]) -> bool:
        """Update the YAML configuration file."""
        logger.info("Writing updated configuration file")
        _config: Dict[str, Any] = self.read_yaml_config()
        _config.update(kwargs)
        try:
            self.write_yaml_config(_config)
            self.update_config()
        except Exception as e:
            logger.error(e)
            return False
        return True

    def get_env_vars(self, prefix: str = "cloudendure") -> Dict[str, any]:
        """Get all environment variables starting with CLOUDENDURE_."""
        prefix: str = prefix.strip("_")
        logger.info("Loading all environment variables starting with (%s)", prefix)
        env_vars: Dict[str, Any] = {
            x[0].lower().lstrip(prefix.lower()).strip("_"): x[1]
            for x in os.environ.items()
            if x[0].lower().startswith(prefix.lower())
        }
        return env_vars

    def update_config(self) -> None:
        """Update the configuration."""
        self.yaml_config_contents: Dict[str, Any] = self.read_yaml_config()
        self.env_config = self.get_env_vars()
        self.active_config = self.merge_config_dicts(
            [self.yaml_config_contents, self.env_config, self.cli]
        )

    def update_token(self, token: str) -> bool:
        """Update the CloudEndure token.

        Returns:
            bool: Whether or not the operation was successful.

        """
        try:
            self.update_yaml_config({"token": token})
        except Exception as e:
            logger.error(e)
            return False
        return True

    def get_var(self, var: str) -> str:
        """Get the specified environment or config variable.

        Returns:
            str: The variable to be used for the provided configuration env var.

        """
        logger.info("Looking up variable: (%s)", var)
        env_var: str = os.environ.get(var.upper(), "")

        if env_var:
            logger.info("Found Environment Variable - (%s): (%s)", var, env_var)
        else:
            env_var = self.yaml_config_contents.get(var.lower(), "")

        logger.info("Return variable value: (%s)", env_var)
        return env_var
