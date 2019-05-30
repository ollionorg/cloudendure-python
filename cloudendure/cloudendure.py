#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Define the CloudEndure main entry logic."""
import fire

from cloudendure.cloudendure_api.api_client import ApiClient

from .api import CloudEndureAPI
from .config import CloudEndureConfig


class CloudEndure:
    """Define the CloudEndure general object."""

    def __init__(self):
        """Initialize the CloudEndure object.

        This entrypoint is primarily for use with the CLI.

        """
        self.config = CloudEndureConfig()
        self.api = CloudEndureAPI()
        self.api_client = ApiClient()


def main():
    """Define the main entry method for the CLI."""
    # Run CloudEndure via the pipeline object for easy CLI access.
    fire.Fire(CloudEndure)


if __name__ == '__main__':
    main()
