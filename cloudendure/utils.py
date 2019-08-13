# -*- coding: utf-8 -*-
"""Define the CloudEndure utility logic.

Attributes:
    first_cap_re (re.Pattern): The regex pattern to determine the first capital
        letter in a string.
    all_cap_re (re.Pattern): The regex pattern to determine all capital letters
        in a string.

"""
from __future__ import annotations

import re
import time
from datetime import datetime
from typing import Any, Dict

first_cap_re: re.Pattern = re.compile("(.)([A-Z][a-z]+)")
all_cap_re: re.Pattern = re.compile("([a-z0-9])([A-Z])")


def get_time_now() -> Dict[str, Any]:
    """Get the current time in UTC as milliseconds.

    Returns:
        dict: The mapping of time now values in UTC.

    """
    time_now: float = time.time()
    milliseconds_now: int = int(round(time_now * 1000))
    datetime_now: datetime = datetime.fromtimestamp(time_now)
    data: Dict[str, Any] = {
        "seconds": time_now,
        "milliseconds": milliseconds_now,
        "datetime": datetime_now,
    }
    return data


def to_snake_case(value: str) -> str:
    """Convert the provided value from CamelCase to snake_case.

    Args:
        value (str): The string value to convert from CamelCase to snake_case.

    Returns:
        str: The formatted snake_case string.

    """
    string_1: str = first_cap_re.sub(r"\1_\2", value)
    string_2: str = all_cap_re.sub(r"\1_\2", string_1).lower()
    return string_2
