# -*- coding: utf-8 -*-
"""Define the CloudEndure Config related logic."""
import logging
import os
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)
LOG_LEVEL = os.environ.get('CLOUDENDURE_LOG_LEVEL', 'INFO')
logger.setLevel(getattr(logging, LOG_LEVEL))


class CloudEndureConfig:
    """Define the CloudEndure Config object."""

    def __init__(self, *args, **kwargs):
        """Initialize the Environment."""
        logger.info('Initializing the CloudEndure Configuration')
        _config_path = os.environ.get('CLOUDENDURE_CONFIG_PATH', '~/.cloudendure.yaml')
        if _config_path.startswith('~'):
            self.config_path = os.path.expanduser(_config_path)

        _config = Path(self.config_path)
        if not _config.exists():
            print('No CloudEndure YAML configuration found! Creating it at: (%s)', self.config_path)
            self.write_yaml_config(
                config={
                    'host': 'https://console.cloudendure.com',
                    'api_version': 'latest',
                    'auth_ttl': '3600',
                    'username': '',
                    'password': '',
                    'token': '',
                    'session_cookie': '',
                }
            )
        self.update_config()

    def __str__(self):
        """Define the string representation of the CloudEndure API object."""
        return '<CloudEndureAPI>'

    def read_yaml_config(self):
        """Read the CloudEndure YAML configuration file."""
        logger.info('Loading the CloudEndure YAML configuration file')
        with open(self.config_path, 'r') as yaml_stream:
            try:
                config = yaml.safe_load(yaml_stream)
            except yaml.YAMLError as e:
                logger.error('YAMLError during read_yaml_config: %s', str(e))
                config = {}
                # print(e)
        return config

    def write_yaml_config(self, config):
        """Write to the CloudEndure YAML configuration file."""
        logger.info('Writing to the CloudEndure YAML configuration file')
        with open(self.config_path, 'w') as yaml_file:
            try:
                yaml.dump(config, yaml_file, default_flow_style=False)
                logger.info('CloudEndure YAML configuration saved!')
                return True
            except Exception as e:
                logger.error('Exception encountered while writing the CloudEndure YAML configuration file - (%s)', e)
        return False

    def update_yaml_config(self, kwargs):
        logger.info("Writing updated configuration file")
        _config = self.read_yaml_config()
        _config.update(kwargs)
        self.write_yaml_config(_config)
        self.update_config()

    def get_env_vars(self, prefix='cloudendure'):
        """Get all environment variables starting with CLOUDENDURE_."""
        prefix = prefix.strip('_')
        logger.info("Loading all environment variables starting with (%s)", prefix)
        env_vars = {
            x[0].lower().lstrip(prefix.lower()).strip('_'): x[1]
            for x in os.environ.items() if x[0].lower().startswith(prefix.lower())
        }
        return env_vars

    def update_config(self):
        self.yaml_config_contents = self.read_yaml_config()
        self.env_config = self.get_env_vars()
        self.active_config = {**self.yaml_config_contents, **self.env_config}

    def update_token(self, token):
        self.update_yaml_config({'token': token})

    def get_var(self, var):
        """Get the specified environment or config variable."""
        logger.info('Looking up variable: (%s)', var)
        env_var = os.environ.get(var.upper(), '')

        if env_var:
            logger.info('Found Environment Variable - (%s): (%s)', var, env_var)
        else:
            env_var = self.yaml_config_contents.get(var.lower(), '')

        logger.info('Return variable value: (%s)', env_var)
        return env_var
