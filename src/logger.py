# -*- coding: utf-8 -*-

"""Defines the logger class. Used to log messages in the terminal."""


class Logger:
    """Class used for logging messages."""

    def __init__(self, is_verbose: bool) -> None:
        """Initialize object Logger."""
        self.is_verbose = is_verbose

    def __repr__(self) -> str:
        """Return a representation of a Logger object."""
        return f"Logger(is_verbose={self.is_verbose})"

    def verbose(self, msg: str) -> None:
        """Print msg if logger is verbose."""
        if self.is_verbose:
            print(msg)
