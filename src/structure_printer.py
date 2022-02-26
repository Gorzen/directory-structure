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
        self.print_checks = print_checks

    def __repr__(self) -> str:
        return f"StructurePrettyPrinter(print_checks={self.print_checks})"

    def print_dir_structure(self, dir_structure: dict) -> None:
        """Print the total directory structure in a tree-like fashion."""
        directories = assert_list(dir_structure["directories"])

        self.__print_dir_name("My directories", dir_exists=True)
        print(BRANCH)

        self.__print_sub_dirs(directories)

    def __print_sub_dirs(
        self, subdirs: list, prefix: str = "", prefix_path: str = ""
    ) -> None:
        """Prints sub directories."""
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
        """Prints one directory in the tree."""
        name = directory["name"]
        path = prefix_path + directory["path"]
        desc = directory["desc"]

        subdirs = get_subdirs(directory)

        self.__print_dir_name(name, os.path.isdir(path), prefix_name)

        pointer = "│ " if subdirs else "  "

        self.__print_dir_info(desc, path, prefix_info + pointer)
        self.__print_sub_dirs(subdirs, prefix_info, path)

    def __print_dir_name(self, name: str, dir_exists: bool, prefix: str = "") -> None:
        """
        Pretty-print directory name.
        Prints warning if directory doesn't exist.
        """
        warning = (
            ""
            if dir_exists
            else f" {style.BOLD}{style.RED}(doesn't exist){style.RESET}"
        )
        check = (
            f" {style.BOLD}{style.GREEN}(OK: directory exists){style.RESET}"
            if dir_exists and self.print_checks
            else ""
        )
        print(f"{prefix}{style.YELLOW}{style.BOLD}{name}{style.RESET}{warning}{check}")

    @staticmethod
    def __print_dir_info(desc: str, path: str, prefix_info: str) -> None:
        """Pretty-print directory information."""
        print(f"{prefix_info}{style.MAGENTA}Desc:{style.RESET} {desc}")
        print(
            f"{prefix_info}{style.MAGENTA}Path:{style.RESET} {style.CYAN}{path}{style.RESET}"
        )
        print(f"{prefix_info}")


def get_subdirs(directory: dict) -> list:
    """Helper to get a list of subdirs for a directory."""
    subdirs = directory["subdirs"] if "subdirs" in directory else []
    return assert_list(subdirs)


def assert_list(arg: list) -> list:
    """Check arg is a list and return it. If it's not a list, raise error."""
    if not isinstance(arg, list):
        raise ValueError(f"{arg} is not a list.")

    return arg
