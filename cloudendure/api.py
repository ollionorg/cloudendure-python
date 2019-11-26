# -*- coding: utf-8 -*-
"""Define the CloudEndure API wrapper related logic.

Attributes:
    API_VERSION (str): The CloudEndure API version to be used.
    AUTH_TTL (str): The authentication token expiration in seconds. Defaults to: 3600.
    HOST (str): The CloudEndure API URI. Defaults to: https://console.cloudendure.com
    logger (logging.Logger): The default logger for the module.

"""
from __future__ import annotations

import datetime
import json
import logging
import os
from typing import Any, Dict, List
from webbrowser import open_new_tab

import requests
from requests.models import Response
from requests.sessions import Session

from cloudendure.config import CloudEndureConfig
from cloudendure.exceptions import CloudEndureException
from cloudendure.utils import get_user_agent

HOST: str = os.environ.get("CLOUDENDURE_HOST", "https://console.cloudendure.com")
API_VERSION: str = os.environ.get("CLOUDENDURE_API_VERSION", "latest").lower()
AUTH_TTL: datetime.timedelta = datetime.timedelta(
    seconds=int(os.environ.get("CLOUDENDURE_AUTH_TTL", "3600"))
)  # Default to 60 minutes.
METHOD_TYPES: List[str] = ["get", "post", "patch", "delete", "put"]

logger: logging.Logger = logging.getLogger(__name__)


class CloudEndureAPI:
    """Define the CloudEndure API base.

    Attributes:
        api_endpoint (str): The CloudEndure API endpoint to be used for API calls.
        credentials (dict): The mapping of CloudEndure credentials.
        session (requests.Session): The requests Session to be used throughout the lifecycle
            of this API interaction.

    """

    TOP_LEVEL: List[str] = ["projects", "blueprints"]

    def __init__(self, config: CloudEndureConfig, *args, **kwargs) -> None:
        """Initialize the CloudEndure API client.

        Attributes:
            time_now (datetime): The datetime now in UTC.

        """
        time_now: datetime.datetime = datetime.datetime.utcnow()

        self.api_endpoint: str = f"{HOST}/api/{API_VERSION}"
        self.config: CloudEndureConfig = config

        self.projects: List[str] = []
        self.session: Session = requests.Session()
        _xsrf_token: str = self.config.active_config.get("token", "")
        self.session.headers: Dict[str, str] = {
            "Content-Type": "application/json",
            "Accept": "text/plain",
            "User-Agent": get_user_agent(),
        }
        self.timestamps: Dict[str, Any] = {
            "created": time_now,
            "updated": time_now,
            "last_call": time_now,
        }

        if _xsrf_token:
            self.session.headers.update({"X-XSRF-TOKEN": _xsrf_token})

    def login(self, username: str = "", password: str = "", token: str = "") -> bool:
        """Login to the CloudEndure API console.

        Args:
            username (str): The CloudEndure username to be used.
                Defaults to the environment specific default.
            password (str): The CloudEndure password to be used.
                Defaults to the environment specific default.
            token (str): The CloudEndure token to be used. This argument takes precedence.
                If provided, username and password will not be used.
                Defaults to the environment specific default.

        Attributes:
            endpoint (str): The CloudEndure API endpoint to be used.
            _username (str): The CloudEndure API username.
            _password (str): The CloudEndure API password.
            _token (str): The CloudEndure API token.
            _auth (dict): The CloudEndure API username/password dictionary map.
            response (requests.Response): The CloudEndure API login request response object.
            _xsrf_token (str): The XSRF token to be used for subsequent API requests.

        TODO:
            * Verify default XSRF-Token TTL and check validity before performing
                subsequent authentication requests.

        """
        _username: str = self.config.active_config["username"] or username
        _password: str = self.config.active_config["password"] or password
        _token: str = self.config.active_config["user_api_token"] or token
        _auth: Dict[str, str] = {}

        if _token:
            _auth["userApiToken"] = _token
        elif _username and _password:
            _auth = {"username": _username, "password": _password}
        else:
            print("You must configure your authentication credentials!")
            return False

        # Attempt to login to the CloudEndure API via a POST request.
        response: requests.Response = self.api_call(
            "login", "post", data=json.dumps(_auth)
        )

        # Check whether or not the request was successful.
        if response.status_code not in [200, 307]:
            if response.status_code == 401:
                print(
                    "\nBad CloudEndure Credentials! Check your username/password and try again!\n"
                )
            elif response.status_code == 402:
                print(
                    "\nNo CloudEndure License! Please configure your account and try again!\n"
                )
            elif response.status_code == 429:
                print(
                    "\nCloudEndure authentication failure limit reached! Please try again later!\n"
                )
            return False

        # Grab the XSRF token received from the response, as stored in cookies.
        # _xsrf_token: str = str(response.cookies["XSRF-TOKEN"])
        _xsrf_token: str = str(response.cookies.get("XSRF-TOKEN", ""))
        if not _xsrf_token:
            raise CloudEndureException("Failed to fetch a token from CloudEndure!")

        # Strip the XSRF token of wrapping double-quotes from the cookie.
        if _xsrf_token.startswith('"') and _xsrf_token.endswith('"'):
            _xsrf_token: str = _xsrf_token[1:-1]

        # Set the XSRF token data on the CloudEndureAPI object.
        time_now: datetime.datetime = datetime.datetime.utcnow()
        self.config.update_token(_xsrf_token)
        self.session.headers.update({"X-XSRF-TOKEN": _xsrf_token})
        self.timestamps["last_call"] = time_now
        return True

    @staticmethod
    def get_endpoint(
        path: str,
        api_version: str = "latest",
        host: str = "https://console.cloudendure.com",
    ) -> str:
        """Build the endpoint path.

        Returns:
            str: The CloudEndure API endpoint to be used.

        """
        return f"{host}/api/{api_version}/{path}"

    def api_call(
        self, path: str, method: str = "get", data: Dict[str, Any] = None
    ) -> Response:
        """Handle CloudEndure API calls based on the defined parameters.

        Args:
            path (str): The path to be used to perform the call.

        Keyword Args:
            method (str): The API method call to be performed. i.e.: get,
            data (dict): The data dictionary to be used to perform the request.

        Returns:
            requests.models.Response: The CloudEndure API response.

        """
        method: str = method.lower()  # Ensure the provided method is lowercase.

        if data is None:
            data: Dict[str, Any] = {}

        if method not in METHOD_TYPES:
            print("Please specify a valid method type! Must be one of: ", METHOD_TYPES)
            return Response()

        if method not in ["get", "delete"] and not data:
            print(
                "Paramater mismatch! If calling anything other than get or delete provide data!"
            )
            return Response()

        # Attempt to call the CloudEndure API.
        try:
            ce_call = getattr(self.session, method)
            _path = self.get_endpoint(path)
            return ce_call(_path, data=data)
        except Exception as e:
            print(f"Exception encountered in CloudEndure API call: ({e})")
        return Response()

    def check_creds(self, login: bool = True) -> Dict[str, str]:
        """Check the credential TTL."""
        threshold: datetime.datetime = datetime.datetime.utcnow() - AUTH_TTL

        if threshold < self.config.active_config.get("last_updated", 0):
            if login:
                is_valid: bool = self.login()
                if is_valid:
                    return {"status": "updated"}
            return {"status": "expired"}
        return {"status": "valid"}

    def post_endpoint(self, path: str = "") -> Response:
        """Create a POST request against the specified path."""
        response: requests.Response = self.session.post(f"{self.api_endpoint}/{path}")
        return response

    def get_projects(self, current_project: str = "") -> List[Any]:
        """Get the CloudEndure projects associated with the authenticated account."""
        self.login()
        response: requests.Response = self.session.get(f"{self.api_endpoint}/projects")
        data: Dict[str, Any] = response.json()
        status_code: int = response.status_code

        if status_code not in [200]:
            raise CloudEndureException()
        projects: List[Any] = data["items"]
        self.projects: List[Any] = projects

        if current_project:
            return list(
                filter(lambda project: project["name"] == current_project, projects)
            )

        return projects

    @classmethod
    def docs(self) -> str:
        """Open the CloudEndure API documentation page."""
        docs_url: str = os.environ.get(
            "CLOUDENDURE_API_DOCS", "https://console.cloudendure.com/api_doc/apis.html"
        )
        open_new_tab(docs_url)
        return docs_url
