# -*- coding: utf-8 -*-
"""Define the CloudEndure utility logic.

Attributes:
    first_cap_re ():
    all_cap_re ():

"""
import re
import time
from datetime import datetime
from typing import Any, Dict

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def get_time_now() -> Dict[str, Any]:
    """Get the current time in UTC as milliseconds."""
    time_now = time.time()
    data = {
        'seconds': time_now,
        'milliseconds': int(round(time_now * 1000)),
        'datetime': datetime.fromtimestamp(time_now),
    }
    return data


def to_snake_case(value: str) -> str:
    """Convert the provided value from CamelCase to snake_case."""
    s1 = first_cap_re.sub(r'\1_\2', value)
    return all_cap_re.sub(r'\1_\2', s1).lower()
