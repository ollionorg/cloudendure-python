# -*- coding: utf-8 -*-
"""Define the Lambda specific exceptions."""
from __future__ import annotations


class LambdaException(Exception):
    """Define the generic AWS Lambda exception."""

    pass


class InvalidPayload(LambdaException):
    """Define the exception to be raised when an invalid payload is encountered."""

    pass


class ImproperlyConfigured(LambdaException):
    """Define the exception to be raised if the environment is improperly configured or missing."""

    pass
