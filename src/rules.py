# -*- coding: utf-8 -*-

"""Defines all the different rules for the directory structure."""

from abc import ABC, abstractmethod

import check


class Rule(ABC):
    """A rule for the directory structure."""

    key: str
    name: str

    def __repr__(self) -> str:
        """Return a representation of a Rule object."""
        return "Rule()"

    @abstractmethod
    def check(self, path: str) -> bool:
        """Check that rule is valid for the directory located at path."""
        return NotImplemented


class NoUnknownDirectories(Rule):
    """No unknown (not declared in the directory structure) directories allowed rule."""

    key = "noUnknownDirectories"
    name = "No unknown directories"

    def __repr__(self) -> str:
        """Return a representation of a NoUnknownDirectories object."""
        return "NoUnknownDirectories()"

    def check(self, path: str) -> bool:
        """Check that rule is valid for the directory located at path."""
        return True


class NoVisibleFiles(Rule):
    """No visible files allowed rule."""

    key = "noVisibleFiles"
    name = "No visible files"

    def __repr__(self) -> str:
        """Return a representation of a NoVisibleFiles object."""
        return "NoVisibleFiles()"

    def check(self, path: str) -> bool:
        """Check that rule is valid for the directory located at path."""
        return True


class NoHiddenFiles(Rule):
    """No hidden files allowed rule."""

    key = "noHiddenFiles"
    name = "No hidden files"

    def __repr__(self) -> str:
        """Return a representation of a NoHiddenFiles object."""
        return "NoHiddenFiles()"

    def check(self, path: str) -> bool:
        """Check that rule is valid for the directory located at path."""
        return True


# All the defined rules
ALL_RULES = [NoUnknownDirectories(), NoVisibleFiles(), NoHiddenFiles()]


def check_rules(
    directory: dict,
    rules_config: dict,
    dir_path: str,
    print_checks: bool,
    prefix_print: str,
) -> bool:
    """Check all rules pass for a given directory.

    Keyword arguments:
    directory    -- The directory
    rules_config -- The rules config
    dir_path     -- The directory's path
    print_checks -- Wether to print the rules checked or not
    prefix_print -- Prefix for the checks printed
    """
    all_rules_pass = True

    for rule in ALL_RULES:
        # Find if we should check the rule or not
        check_rule = directory.get(rule.key, rules_config[rule.key])

        if check_rule:
            rule_checked = rule.check(dir_path)
            all_rules_pass = all_rules_pass and rule_checked
            info = ""
        else:
            rule_checked = True
            info = " (rule set to false, check will always pass)"

        if print_checks:
            check_msg = (
                check.success(f"{rule.name}{info}", print_checks)
                if rule_checked
                else check.failure(f"{rule.name}{info}", print_checks)
            )
            print(f"{prefix_print}{check_msg}")

    return all_rules_pass
