#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The main file of the project manage-directories.

Run it to see and check your directory structure vs your config.
"""

# TODOS:
# Add rule for unknown directories
# Change 'check' function names to assert if they throw erros and don't return bool
# Add option to give config path
# Implement options
# Use tox?
# Add GitHub actions
# Add badges in README for all python checkers
# Add logger with verbose:
#   log OK  - dir - no hidden file
#   or   NOT OK - dir - [list of files]

import argparse
import os
import yaml

from structure_printer import StructurePrettyPrinter, get_subdirs
from rules import ALL_RULES


def check_rules_equal(dir_structure: dict) -> None:
    """Check config rules and implemented rules are the same."""
    config_rules = list(dir_structure["rules"].keys())
    script_rules = list(map(lambda rule: rule.key, ALL_RULES))

    if config_rules != script_rules:
        raise ValueError(
            f"""Config rules and rules implemented are different !
        Config rules: {config_rules}
        Implemented rules: {script_rules}"""
        )


def check_rules0(dir_structure: dict) -> None:
    """Check user directories follow the rules specified in the config."""
    check_rules_equal(dir_structure)

    def check_directory(directory, prefix_path=""):
        path = prefix_path + directory["path"]

        for rule in ALL_RULES:
            rule.check(path)

        for subdir in get_subdirs(directory):
            check_directory(subdir, prefix_path)

    directories = dir_structure["directories"]

    for directory in directories:
        check_directory(directory)


def main(print_checks: bool, check_rules: bool, verbose: bool) -> None:
    """Run the program."""
    dir_structure_path = os.path.join(
        os.path.dirname(__file__), "..", "config", "directories_structure.yml"
    )

    print(
        f"""
        print_checks={print_checks}
        check_rules={check_rules}
        verbose={verbose}
        """
    )

    with open(dir_structure_path, "r", encoding="utf-8") as dir_structure_file:
        try:
            dir_structure = yaml.safe_load(dir_structure_file)

            pretty_printer = StructurePrettyPrinter(check_rules, print_checks)

            pretty_printer.print_dir_structure(dir_structure)

            check_rules0(dir_structure)

        except yaml.YAMLError as exc:
            print("Error when loading yaml:")
            print(exc)


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser(description="Monitor your directory structure.")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="verbose. Useful when checking rules.",
    )
    parser.add_argument(
        "--check-rules", action="store_true", help="Check directory rules."
    )
    parser.add_argument(
        "--print-checks",
        action="store_true",
        help="Print in the tree all the checks performed.",
    )
    args = parser.parse_args()

    # Run main
    main(args.print_checks, args.check_rules, args.verbose)
