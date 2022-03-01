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
# Implement rules
# Use tox?
# Add README
# Add GitHub actions
# Add badges in README for all python checkers
# Improve check.py, a bit too much code to print the success msg.
#   Add another function for printing?
# Add logger with verbose for rules:
#   log OK  - dir - no hidden file
#   or   NOT OK - dir - [list of files]

import argparse
import os
import yaml

from logger import Logger
from structure_printer import StructurePrettyPrinter
from rules import ALL_RULES


def assert_rules_equal(dir_structure: dict) -> None:
    """Assert config rules and implemented rules are the same."""
    config_rules = list(dir_structure["rules"].keys())
    script_rules = list(map(lambda rule: rule.key, ALL_RULES))

    if config_rules != script_rules:
        raise ValueError(
            f"""Config rules and rules implemented are different !
        Config rules: {config_rules}
        Implemented rules: {script_rules}"""
        )


def main(print_checks: bool, check_rules: bool, verbose: bool) -> None:
    """Run the program."""
    dir_structure_path = os.path.join(
        os.path.dirname(__file__), "..", "config", "directories_structure.yml"
    )

    with open(dir_structure_path, "r", encoding="utf-8") as dir_structure_file:
        try:
            dir_structure = yaml.safe_load(dir_structure_file)

            assert_rules_equal(dir_structure)

            logger = Logger(is_verbose=verbose)

            pretty_printer = StructurePrettyPrinter(check_rules, print_checks, logger)

            pretty_printer.print_dir_structure(dir_structure)

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
