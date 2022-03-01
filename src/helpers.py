# -*- coding: utf-8 -*-

"""Various helper functions."""

import os


def expand_user(path: str) -> str:
    """Expand user of given path."""
    return os.path.expanduser(path)


def is_dir(path: str) -> bool:
    """Return true if path is a directory, false otherwise."""
    return os.path.isdir(path)


def assert_dir(path: str) -> None:
    """Raise an error if path is not a directory."""
    if not os.path.isdir(path):
        raise ValueError(f"{path} is not a directory.")


def get_dirs(path: str) -> list:
    """Get list of directories in a directory."""
    assert_dir(path)
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


def get_files(path: str) -> list:
    """Get list of files in a directory."""
    assert_dir(path)
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


def get_subdirs(directory: dict) -> list:
    """Get list of sub directories for a directory."""
    subdirs = directory["subdirs"] if "subdirs" in directory else []
    return assert_list(subdirs)


def assert_list(arg: list) -> list:
    """Check arg is a list and return it. If it's not a list, raise error."""
    if not isinstance(arg, list):
        raise ValueError(f"{arg} is not a list.")

    return arg
