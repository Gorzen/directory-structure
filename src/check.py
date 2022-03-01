# -*- coding: utf-8 -*-

"""Helpers to get check messages."""

import style


def success(
    message: str,
    show_checks: bool,
    empty_on_success: bool = False,
    parentheses: bool = False,
    prefix: str = "",
) -> str:
    """Create a successful check message.

    Keyword arguments:
    message          -- The message
    show_checks      -- Prefixes the message with 'OK: '. Overrides empty_on_success
    empty_on_success -- Return empty on success, overriden by show_checks
    parentheses      -- If message should be in parentheses
    prefix           -- Prefix added to the check message returned
    """
    if show_checks:
        message = f"OK: {message}"
    if parentheses:
        message = f"({message})"

    message = f"{prefix}{style.BOLD}{style.GREEN}{message}{style.RESET}"

    if empty_on_success and not show_checks:
        # TODO: If printed, it will still put a newline
        return ""

    return message


def failure(
    message: str, show_checks: bool, parentheses: bool = False, prefix: str = ""
) -> str:
    """Create a failure check message.

    Keyword arguments:
    message          -- The message
    show_checks      -- Prefixes the message with 'NOT OK: '
    parentheses      -- If message should be in parentheses
    prefix           -- Prefix added to the check message returned
    """
    if show_checks:
        message = f"NOT OK: {message}"
    if parentheses:
        message = f"({message})"

    return f"{prefix}{style.BOLD}{style.RED}{message}{style.RESET}"
