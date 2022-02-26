# -*- coding: utf-8 -*-

"""Pretty printer for directory strucure, similar to the tree command."""

import style

# prefix components
SPACE = "    "
BRANCH = "│   "

# pointers for names
TEE = "├── "
LAST = "└── "


def print_dir_structure(dir_structure: dict) -> None:
    """Print the total directory structure in a tree-like fashion."""
    directories = assert_list(dir_structure["directories"])

    print_dir_name("My directories")
    print(BRANCH)

    print_sub_dirs(directories)


def print_sub_dirs(subdirs: list, prefix: str = "", prefix_path: str = "") -> None:
    """Prints sub directories."""
    num_subdirs = len(subdirs)

    for i, directory in enumerate(subdirs):
        if i == num_subdirs - 1:
            print_directory(directory, prefix + LAST, prefix + SPACE, prefix_path)
        else:
            print_directory(directory, prefix + TEE, prefix + BRANCH, prefix_path)


def print_directory(
    directory: dict, prefix_name: str = "", prefix_info: str = "", prefix_path: str = ""
) -> None:
    """Prints one directory in the tree."""
    name = directory["name"]
    path = prefix_path + directory["path"]
    desc = directory["desc"]

    subdirs = get_subdirs(directory)

    print_dir_name(name, prefix_name)

    pointer = "│ " if subdirs else "  "

    print_dir_info(desc, path, prefix_info + pointer)
    print_sub_dirs(subdirs, prefix_info, path)


def print_dir_name(name: str, prefix: str = "") -> None:
    """Pretty-print directory name."""
    print(f"{prefix}{style.YELLOW}{style.BOLD}{name}{style.RESET}")


def print_dir_info(desc: str, path: str, prefix_info: str) -> None:
    """Pretty-print directory information."""
    print(f"{prefix_info}{style.MAGENTA}Desc:{style.RESET} {desc}")
    print(
        f"{prefix_info}{style.MAGENTA}Path:{style.RESET} {style.CYAN}{path}{style.RESET}"
    )
    print(f"{prefix_info}")


def get_subdirs(directory: dict) -> list:
    """Helper to get a list of subdirs for a directory."""
    subdirs = assert_list(directory["subdirs"]) if "subdirs" in directory else []
    return subdirs


def assert_list(arg: list) -> list:
    """Check arg is a list and return it. If it's not a list, raise error."""
    if not isinstance(arg, list):
        raise ValueError(f"{arg} is not a list.")

    return arg
