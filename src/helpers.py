# -*- coding: utf-8 -*-

"""Various helper functions."""

import os


def is_dir(path: str) -> bool:
    """Return true if path is a directory, false otherwise."""
    expanded_path = os.path.expanduser(path)
    return os.path.isdir(expanded_path)


def get_subdirs(directory: dict) -> list:
    """Get list of sub directories for a directory."""
    subdirs = directory["subdirs"] if "subdirs" in directory else []
    return assert_list(subdirs)


def assert_list(arg: list) -> list:
    """Check arg is a list and return it. If it's not a list, raise error."""
    if not isinstance(arg, list):
        raise ValueError(f"{arg} is not a list.")

    return arg
