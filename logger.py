# -*- coding: utf-8 -*-

"""Defines the logger class. Used to log messages in the terminal"""


class Logger:
    """Class used for logging at different levels."""

    def __init__(self, is_verbose):
        self.is_verbose = is_verbose

    def __repr__(self):
        return f"Logger(is_verbose={self.is_verbose})"

    def verbose(self, msg):
        """Prints msg if logger is verbose."""
        if self.is_verbose:
            print(msg)