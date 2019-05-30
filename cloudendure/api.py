# -*- coding: utf-8 -*-
"""Define the CloudEndure API wrapper related logic.

Attributes:
    API_VERSION (str): The CloudEndure API version to be used.
    AUTH_TTL (str): The authentication token expiration in seconds. Defaults to: 3600.
    HOST (str): The CloudEndure API URI. Defaults to: https://console.cloudendure.com
    logger (logging.Logger): The default logger for the module.

"""
import datetime
import logging
import os
from typing import Any, Dict, List
from webbrowser import open_new_tab

import requests

from .config import CloudEndureConfig
from .exceptions import CloudEndureException, CloudEndureUnauthorized
from .models import Machine, Project

HOST: str = os.environ.get('CLOUDENDURE_HOST', 'https://console.cloudendure.com')
API_VERSION: str = os.environ.get('CLOUDENDURE_API_VERSION', 'latest').lower()
AUTH_TTL = datetime.timedelta(seconds=int(os.environ.get('CLOUDENDURE_AUTH_TTL', '3600')))  # Default to 60 minutes.

logger = logging.getLogger(__name__)


class CloudEndureAPI:
    """Define the CloudEndure API base.

    Attributes:
        api_endpoint (str): The CloudEndure API endpoint to be used for API calls.
        credentials (dict): The mapping of CloudEndure credentials.
        session (requests.Session): The requests Session to be used throughout the lifecycle
            of this API interaction.

    """

    TOP_LEVEL: List[str] = ['projects', 'blueprints']

    def __init__(self, *args, **kwargs):
        """Initialize the CloudEndure API client.

        Attributes:
            time_now (datetime): The datetime now in UTC.

        """
        time_now = datetime.datetime.utcnow()

        # if config is None:
        #     config = {
        #         'host': os.environ.get('CLOUDENDURE_HOST', 'https://console.cloudendure.com').lower(),
        #         'api_version': os.environ.get('CLOUDENDURE_API_VERSION', 'latest').lower(),
        #         'auth_ttl': datetime.timedelta(seconds=int(os.environ.get('CLOUDENDURE_AUTH_TTL', '3600'))),
        #     }

        self.api_endpoint: str = f'{HOST}/api/{API_VERSION}'
        self.config = CloudEndureConfig()
        # self.credentials = {
        #     'username': os.environ.get('CLOUDENDURE_USERNAME', ''),
        #     'password': os.environ.get('CLOUDENDURE_PASSWORD', ''),
        #     'token': os.environ.get('CLOUDENDURE_TOKEN', ''),
        #     'last_updated': time_now,
        # }

        # params = ['username', 'password', 'token']
        # for param in params:
        #     if not self.credentials.get(param, ''):
        #         self.credentials[param] = self.config.get(param, '')

        self.projects: List[str] = []
        self.session = requests.Session()
        _xsrf_token: str = self.config.active_config.get('token', '')
        self.session.headers: Dict[str, str] = {'Content-Type': 'application/json', 'Accept': 'text/plain', }
        self.timestamps: Dict[str, Any] = {'created': time_now, 'updated': time_now, 'last_call': time_now}

        if _xsrf_token:
            self.session.headers.update({'X-XSRF-TOKEN': _xsrf_token})

    def login(self, username='', password=''):
        """Login to the CloudEndure API console.

        Args:
            username (str): The CloudEndure username to be used.
                Defaults to the environment specific default.
            password (str): The CloudEndure password to be used.
                Defaults to the environment specific default.

        Attributes:
            endpoint (str): The CloudEndure API endpoint to be used.
            _username (str): The CloudEndure API username.
            _password (str): The CloudEndure API password.
            _auth (dict): The CloudEndure API username/password dictionary map.
            response (requests.Response): The CloudEndure API login request response object.
            _xsrf_token (str): The XSRF token to be used for subsequent API requests.

        """
        endpoint: str = 'login'
        _username: str = self.config.active_config['username'] or username
        _password: str = self.config.active_config['password'] or password
        _auth: Dict[str, str] = {'username': _username, 'password': _password}

        # Attempt to login to the CloudEndure API via a POST request.
        response: requests.Response = self.session.post(f'{self.api_endpoint}/{endpoint}', json=_auth)
        print('response: ', response, response.status_code)

        # Check whether or not the request was successful.
        if response.status_code not in [200, 307]:
            if response.status_code == 401:
                logger.error('Bad CloudEndure Credentials! Check your username/password and try again!')
            elif response.status_code == 402:
                logger.error('No CloudEndure License! Please configure your account and try again!')
            elif response.status_code == 429:
                logger.error('CloudEndure authentication failure limit reached! Please try again later!')
            raise CloudEndureUnauthorized()

        print('response: ', response, response.cookies)
        _xsrf_token: str = str(response.cookies['XSRF-TOKEN'])

        # Strip the XSRF token of wrapping double-quotes from the cookie.
        if _xsrf_token.startswith('"') and _xsrf_token.endswith('"'):
            _xsrf_token: str = _xsrf_token[1:-1]

        # Set the XSRF token data on the CloudEndureAPI object.
        time_now = datetime.datetime.utcnow()
        self.config.update_token(_xsrf_token)
        self.session.headers.update({'X-XSRF-TOKEN': _xsrf_token})
        self.timestamps['last_call'] = time_now
        return True

    def check_creds(self, login=True):
        threshold = datetime.datetime.utcnow() - AUTH_TTL

        if threshold < self.config.active_config.get('last_updated', 0):
            if login:
                is_valid: bool = self.login()
                if is_valid:
                    return {'status': 'updated'}
            return {'status': 'expired'}
        return {'status': 'valid'}

    def get_endpoint(self, path='', child_key='items'):
        response: requests.Response = self.session.get(f'{self.api_endpoint}/{path}')
        data: Dict[str, Any] = response.json()
        status_code: int = response.status_code
        print('status: ', status_code)
        print('data: ', data)
        if status_code not in [200, ]:
            raise CloudEndureException()
        return data.get(child_key, [])

    def post_endpoint(self, path=''):
        response: requests.Response = self.session.post(f'{self.api_endpoint}/{path}')
        return response

    def get_projects(self, current_project=''):
        """Get the CloudEndure projects associated with the authenticated account."""
        self.login()
        response: requests.Response = self.session.get(f'{self.api_endpoint}/projects')
        data: Dict[str, Any] = response.json()
        status_code: int = response.status_code
        print('Status: ', status_code)
        if status_code not in [200, ]:
            raise CloudEndureException()
        projects: List[Any] = data['items']
        self.projects: List[Any] = projects

        if current_project:
            return list(filter(lambda project: project['name'] == current_project, projects))

        return projects

    def get_project(self, project):
        found_projects: List[Any] = self.get_endpoint(path='projects')
        if not project:
            return found_projects[0]
        try:
            return next(found_project for found_project in found_projects if found_project['name'] == project)
        except Exception as e:
            # Cowardly catch all Exception here.
            logger.error(f'{e} - get_project - attempting to find the provided project in account projects.')
            return {}

    def get_token(self, project=''):
        """Get the CloudEndure project installation token."""
        found_project: Dict[str, Any] = self.get_project(project)
        return found_project[0]['agentInstallationToken']

    @classmethod
    def docs(self):
        """Open the CloudEndure API documentation page."""
        docs_url: str = os.environ.get('CLOUDENDURE_API_DOCS', 'https://console.cloudendure.com/api_doc/apis.html')
        open_new_tab(docs_url)
        return docs_url

    # def get_token(args):
    #     # This function fetch the project installation token
    #     # Usage: get_token(args)
    #     #       'args' is script user input (args.user, args.password, args.agentname)
    #     #
    #     # Returns:      -1 on failure
    #     print "Fetching the installation token..."
    #     session, resp, endpoint = login(args)
    #     if session == -1:
    #         print "Failed to login"
    #         return -1

    #     project_name = args.project

    #     projects_resp = session.get(url=HOST+endpoint+'projects')
    #     projects = json.loads(projects_resp.content)['items']

    #     project = [p for p in projects if project_name==p['name']]
    #     if not project:
    #         print 'Error! No project with name ' + args.project+ ' found'
    #         return -1

    #     return project[0]['agentInstallationToken']


# class CloudEndureCredentials:
#     """Define the CloudEndure Credentials object."""

#     def __init__(self, *args, **kwargs):
#         """Initialize the CloudEndure credentials."""
#         self.
