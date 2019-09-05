# -*- coding: utf-8 -*-
"""Define the CloudEndure API client related logic."""
from __future__ import annotations

from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient as requests_client

from .config import CloudEndureConfig


class CloudEndureClient:
    """Define the CloudEndure API client."""

    def __init__(
        self: CloudEndureClient, config: CloudEndureConfig, project_id: str = ""
    ) -> None:
        """Initialize the CloudEndure API client."""
        self.config = config
        self.project_id = project_id
        self.swagger_api_url = self.config.active_config.get(
            "swagger_api_json_url", "https://console.cloudendure.com/api_doc/apis.json"
        )
        self.http_client = requests_client()
        self.http_client.set_api_key(
            "console.cloudendure.com",
            self.config.active_config.get("token", ""),
            param_name="X-XSRF-TOKEN",
            param_in="header",
        )
        self.cursor = SwaggerClient.from_url(
            self.swagger_api_url, http_client=self.http_client
        )
