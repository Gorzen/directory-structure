# -*- coding: utf-8 -*-

"""Pretty printer for directory strucure, similar to the tree command."""

import os

import check
from logger import Logger
from rules import ALL_RULES
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
    check_rules: bool

    # Rules config
    rules_config: dict

    # Global checkers
    all_dirs_exist: bool
    all_rules_pass: bool

    def __init__(self, check_rules: bool, print_checks: bool, logger: Logger) -> None:
        """Initialize object StructurePrettyPrinter."""
        self.check_rules = check_rules
        self.print_checks = print_checks
        self.logger = logger

    def __repr__(self) -> str:
        """Return a representation of a StructurePrettyPrinter object."""
        return f"StructurePrettyPrinter(print_checks={self.print_checks})"

    def print_dir_structure(self, dir_structure: dict) -> None:
        """Print the total directory structure in a tree-like fashion."""
        # Init global checkers
        self.all_dirs_exist = True
        self.all_rules_pass = True

        # Set rules config
        self.rules_config = dir_structure["rules"]

        # Get top-level directories
        directories = assert_list(dir_structure["directories"])

        # Print root
        self.__print_dir_name("My directories")
        print(BRANCH)

        # Print directories
        self.__print_sub_dirs(directories)

        # Print info about global checkers
        self.__print_global_checkers()

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
        # Get mandatory fields
        name = directory["name"]
        path = prefix_path + directory["path"]
        desc = directory["desc"]

        # Get sub directories
        subdirs = get_subdirs(directory)

        # Print directory name
        dir_exists = is_dir(path)
        dir_check = (
            check.success("directory exists", self.print_checks, True, True, " ")
            if dir_exists
            else check.failure("directory doesn't exist", self.print_checks, True, " ")
        )
        self.__print_dir_name(name, prefix_name, dir_check)

        # Print directory info
        pointer = "│ " if subdirs else "  "
        self.__print_dir_info(desc, path, prefix_info + pointer)

        # Check rules
        if self.check_rules:
            self.__check_rules(directory, path, prefix_info + pointer)

        # Print padding line
        print(f"{prefix_info + pointer}")

        # Print sub directories
        self.__print_sub_dirs(subdirs, prefix_info, path)

    def __check_rules(self, directory: dict, dir_path: str, prefix_print: str) -> None:
        for rule in ALL_RULES:
            # Find if we should check the rule or not
            check_rule = directory.get(rule.key, self.rules_config[rule.key])

            if check_rule:
                rule_checked = rule.check(dir_path)
                self.all_rules_pass = self.all_rules_pass and rule_checked
                info = ""
            else:
                rule_checked = True
                info = " (rule set to false, check will always pass)"

            if self.print_checks:
                check_msg = (
                    check.success(f"{rule.name}{info}", self.print_checks)
                    if rule_checked
                    else check.failure(f"{rule.name}{info}", self.print_checks)
                )
                print(f"{prefix_print}{check_msg}")

    def __print_global_checkers(self) -> None:
        # Print all_dirs_exist check
        if self.all_dirs_exist:
            print(check.success("All directories exist !", self.print_checks, True))
        else:
            print(check.failure("Not all directories exist.", self.print_checks))

        # Print all_rules_pass check
        if self.check_rules:
            if self.all_rules_pass:
                print(check.success("All rules pass !", self.print_checks))
            else:
                print(check.failure("Not all rules pass.", self.print_checks))

    @staticmethod
    def __print_dir_name(name: str, prefix: str = "", check_msg: str = "") -> None:
        """Pretty-print directory name."""
        print(f"{prefix}{style.YELLOW}{style.BOLD}{name}{style.RESET}{check_msg}")

    @staticmethod
    def __print_dir_info(desc: str, path: str, prefix_info: str) -> None:
        """Pretty-print directory information."""
        # Print description
        print(f"{prefix_info}{style.MAGENTA}Desc:{style.RESET}", end=" ")
        print(f"{desc}")

        # Print path
        print(f"{prefix_info}{style.MAGENTA}Path:{style.RESET}", end=" ")
        print(f"{style.CYAN}{path}{style.RESET}")


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
