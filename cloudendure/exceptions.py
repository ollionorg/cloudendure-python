# -*- coding: utf-8 -*-
"""Define the CloudEndure exceptions."""
from __future__ import annotations


class CloudEndureException(Exception):
    """Define the structure of a CloudEndure exception."""

    pass


class CloudEndureHTTPException(CloudEndureException):
    """Define the CloudEndure exception for unauthorized content."""

    pass


class CloudEndureUnauthorized(CloudEndureHTTPException):
    """The CloudEndure HTTP exception (401) was encountered for the request due to an unauthenticated request."""

    pass


class CloudEndureForbidden(CloudEndureHTTPException):
    """The CloudEndure HTTP exception (403) was encountered because the current user is not allowed access."""

    pass


class CloudEndureNotFound(CloudEndureHTTPException):
    """The CloudEndure HTTP exception (404) was encountered for the request due to the object not being found."""

    pass


class CloudEndureMethodNotAllowed(CloudEndureHTTPException):
    """The CloudEndure HTTP exception (405) raised when using a method that is not supported.

    For example: (POST instead of GET).

    """

    pass


class CloudEndureUnprocessableEntity(CloudEndureHTTPException):
    """The CloudEndure HTTP exception (422) was encountered due to invalid input."""

    pass


class CloudEndureInvalidEvent(CloudEndureException):
    """The CloudEndure exception for invalid Event types."""

    pass


class CloudEndureMisconfigured(CloudEndureException):
    """The CloudEndure exception indicating the CLI/Module hasn't been configured properly."""

    pass
