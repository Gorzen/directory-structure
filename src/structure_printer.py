# -*- coding: utf-8 -*-

"""Pretty printer for directory strucure, similar to the tree command."""

import os

import style

# prefix components
SPACE = "    "
BRANCH = "│   "

# pointers for names
TEE = "├── "
LAST = "└── "


class StructurePrettyPrinter:
    """Prints directory structure in a tree-like fashion."""

    print_checks: bool

    def __init__(self, print_checks: bool) -> None:
        """Initialize object StructurePrettyPrinter."""
        self.print_checks = print_checks

    def __repr__(self) -> str:
        """Return a representation of a StructurePrettyPrinter object."""
        return f"StructurePrettyPrinter(print_checks={self.print_checks})"

    def print_dir_structure(self, dir_structure: dict) -> None:
        """Print the total directory structure in a tree-like fashion."""
        directories = assert_list(dir_structure["directories"])

        self.__print_dir_name("My directories")
        print(BRANCH)

        self.__print_sub_dirs(directories)

    def __print_sub_dirs(
        self, subdirs: list, prefix: str = "", prefix_path: str = ""
    ) -> None:
        """Print sub directories."""
        num_subdirs = len(subdirs)

        for i, directory in enumerate(subdirs):
            if i == num_subdirs - 1:
                self.__print_directory(
                    directory, prefix + LAST, prefix + SPACE, prefix_path
                )
            else:
                self.__print_directory(
                    directory, prefix + TEE, prefix + BRANCH, prefix_path
                )

    def __print_directory(
        self,
        directory: dict,
        prefix_name: str = "",
        prefix_info: str = "",
        prefix_path: str = "",
    ) -> None:
        """Print one directory in the tree."""
        name = directory["name"]
        path = prefix_path + directory["path"]
        desc = directory["desc"]

        subdirs = get_subdirs(directory)

        dir_check = self.__is_dir_check(path)
        self.__print_dir_name(name, prefix_name, dir_check)

        pointer = "│ " if subdirs else "  "

        self.__print_dir_info(desc, path, prefix_info + pointer)
        self.__print_sub_dirs(subdirs, prefix_info, path)

    def __is_dir_check(self, path) -> str:
        """Get is_directory check message."""
        dir_exists = is_dir(path)
        check = ""

        if dir_exists and self.print_checks:
            check += f" {style.BOLD}{style.GREEN}"
            check += "(OK: directory exists)"
            check += f"{style.RESET}"

        elif not dir_exists:
            check += f" {style.BOLD}{style.RED}"

            if self.print_checks:
                check += "(NOT OK: directory doesn't exist)"
            else:
                check += "(doesn't exist)"

            check += f"{style.RESET}"

        return check

    @staticmethod
    def __print_dir_name(name: str, prefix: str = "", check: str = "") -> None:
        """Pretty-print directory name."""
        print(f"{prefix}{style.YELLOW}{style.BOLD}{name}{style.RESET}{check}")

    @staticmethod
    def __print_dir_info(desc: str, path: str, prefix_info: str) -> None:
        """Pretty-print directory information."""
        # Print description
        print(f"{prefix_info}{style.MAGENTA}Desc:{style.RESET}", end=" ")
        print(f"{desc}")

        # Print path
        print(f"{prefix_info}{style.MAGENTA}Path:{style.RESET}", end="")
        print(f"{style.CYAN}{path}{style.RESET}")

        # Print padding line
        print(f"{prefix_info}")


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
