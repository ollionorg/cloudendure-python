# -*- coding: utf-8 -*-
"""Define the CloudEndure events."""
from __future__ import annotations

import os
from datetime import datetime
from typing import Any, Dict, List, Tuple

from cloudendure.exceptions import CloudEndureInvalidEvent

EXIT_ON_WARNING: bool = bool(os.environ.get("CLOUDENDURE_EXIT_ON_WARNING", "0"))


class EventHandler:
    """Define the handling of CloudEndure Event objects."""

    def __init__(self, events: List[Any] = None) -> None:
        """Initialize the event handler."""
        self.events: List[Any] = events or []

    def add_event(self, event_type: Tuple[str, str], machine_name, **kwargs) -> bool:
        """Add an event."""
        self.events.append(Event(event_type, machine_name, **kwargs))


class Event:
    """Define the structure of a CloudEndure Event.

    Usage:
        from cloudendure.event import Event
        some_event = Event(Event.EVENT_EXPIRED, somevar="some")

    """

    EVENT_STRUCTURE: Dict[str, str] = {
        "machine_name": "",
        "event_type": "",
        "event_abbreviation": "",
        "timestamp": "",
    }

    # Errorred Event Types
    EVENT_EXPIRED: Tuple[str, str] = ("EXPIRED", "EE")
    EVENT_FAILED: Tuple[str, str] = ("FAILED", "EF")

    ERRORRED_EVENT_TYPES: List[Tuple[str, str]] = [EVENT_EXPIRED, EVENT_FAILED]

    # Successful Event Types
    EVENT_SUCCESSFULLY_LAUNCHED: Tuple[str, str] = ("SUCCESSFULLY_LAUNCHED", "SL")

    SUCCESSFUL_EVENT_TYPES: List[Tuple[str, str]] = [EVENT_SUCCESSFULLY_LAUNCHED]

    # Warned Event Types
    EVENT_IGNORED: Tuple[str, str] = ("IGNORED", "EI")
    EVENT_IN_PROGRESS: Tuple[str, str] = ("IN_PROGRESS", "IP")
    EVENT_ALREADY_LAUNCHED: Tuple[str, str] = ("ALREADY_LAUNCHED", "AL")

    WARNED_EVENT_TYPES: List[Tuple[str, str]] = [
        EVENT_IGNORED,
        EVENT_IN_PROGRESS,
        EVENT_ALREADY_LAUNCHED,
    ]

    EVENT_TYPES: List[
        Tuple[str, str]
    ] = ERRORRED_EVENT_TYPES + SUCCESSFUL_EVENT_TYPES + WARNED_EVENT_TYPES

    def __init__(self, event_type, machine_name: str = "NA", **kwargs) -> None:
        """Initialize the Event."""
        if event_type not in self.EVENT_TYPES:
            raise CloudEndureInvalidEvent(f"Event Type: {event_type} is unrecognized!")

        self.machine_name: str = machine_name.upper()
        self.event_type: Tuple[str, str] = event_type

        exit_code: int = (
            0
            if (
                self.event_type not in self.ERRORRED_EVENT_TYPES
                or self.event_type not in self.WARNED_EVENT_TYPES
                and EXIT_ON_WARNING
            )
            else 1
        )

        self.event_dict: Dict[str, Any] = {
            "event_type_tuple": self.event_type,
            "event_type": self.event_type[0],
            "event_abbreviation": self.event_type[1],
            "machine_name": self.machine_name,
            "timestamp": datetime.now().timestamp(),
            "exit_code": exit_code,
        }

        for k, v in kwargs.items():
            setattr(self, k, v)
            self.event_dict[k] = v
