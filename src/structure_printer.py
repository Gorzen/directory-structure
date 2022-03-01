# -*- coding: utf-8 -*-

"""Pretty printer for directory strucure, similar to the tree command."""

import check
from logger import Logger
from helpers import is_dir, get_subdirs, assert_list, expand_user
from printers import print_dir_info, print_dir_name
import rules

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
        print_dir_name("My directories")
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

        # Check if directory exists
        expanded_path = expand_user(path)
        dir_exists = is_dir(path)
        self.all_dirs_exist = dir_exists and self.all_dirs_exist
        dir_check = (
            check.success("directory exists", self.print_checks, True, True, " ")
            if dir_exists
            else check.failure("directory doesn't exist", self.print_checks, True, " ")
        )

        # Print directory name
        print_dir_name(name, prefix_name, dir_check)

        # Print directory info
        pointer = "│ " if subdirs else "  "
        print_dir_info(desc, path, prefix_info + pointer)

        # Check rules
        if self.check_rules:
            rules_pass = rules.check_rules(
                directory,
                expanded_path,
                self.rules_config,
                self.print_checks,
                prefix_info + pointer,
            )
            self.all_rules_pass = rules_pass and self.all_rules_pass

        # Print padding line
        print(f"{prefix_info + pointer}")

        # Print sub directories
        self.__print_sub_dirs(subdirs, prefix_info, path)

    def __print_global_checkers(self) -> None:
        # Print all_dirs_exist check
        if self.all_dirs_exist:
            msg = check.success("All directories exist !", self.print_checks, True)
            if msg:
                print(msg)
        else:
            print(check.failure("Not all directories exist.", self.print_checks))

        # Print all_rules_pass check
        if self.check_rules:
            if self.all_rules_pass:
                print(check.success("All rules pass !", self.print_checks))
            else:
                print(check.failure("Not all rules pass.", self.print_checks))
