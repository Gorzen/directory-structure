# -*- coding: utf-8 -*-

"""Defines all the different rules for the directory structure."""

from abc import ABC, abstractmethod

import check
from helpers import get_dirs, get_files, get_subdirs, is_dir


class Rule(ABC):
    """A rule for the directory structure."""

    key: str
    name: str

    def __repr__(self) -> str:
        """Return a representation of a Rule object."""
        return "Rule()"

    @abstractmethod
    def check(self, directory: dict, dir_path: str) -> list:
        """
        Check a rule for the given directory.

        Return empty list if rule is valid, otherwise returns a list of reasons
        """
        return NotImplemented


class NoUnknownDirectories(Rule):
    """No unknown (not declared in the directory structure) directories allowed rule."""

    key = "noUnknownDirectories"
    name = "No unknown directories"

    def __repr__(self) -> str:
        """Return a representation of a NoUnknownDirectories object."""
        return "NoUnknownDirectories()"

    def check(self, directory: dict, dir_path: str) -> list:
        """Check that there are no unknown directories in the given directory."""
        if not is_dir(dir_path):
            return ["Directory doesn't exist."]
        subdirs_ = get_subdirs(directory)
        subdirs = set(map(lambda subdir: subdir["path"].split("/")[-1], subdirs_))
        dirs = set(get_dirs(dir_path))
        return list(dirs - subdirs)


class NoHiddenDirectories(Rule):
    """No hidden directories allowed rule."""

    key = "noHiddenDirectories"
    name = "No hidden directories"

    def __repr__(self) -> str:
        """Return a representation of a NoHiddenDirectories object."""
        return "NoHiddenDirectories()"

    def check(self, directory: dict, dir_path: str) -> list:
        """Check that there are no hidden directories in the given directory."""
        if not is_dir(dir_path):
            return ["Directory doesn't exist."]
        dirs = get_dirs(dir_path)
        hidden_dirs = list(filter(lambda dir: dir.startswith("."), dirs))
        return hidden_dirs


class NoVisibleFiles(Rule):
    """No visible files allowed rule."""

    key = "noVisibleFiles"
    name = "No visible files"

    def __repr__(self) -> str:
        """Return a representation of a NoVisibleFiles object."""
        return "NoVisibleFiles()"

    def check(self, directory: dict, dir_path: str) -> list:
        """Check that there are no visible files in the given directory."""
        if not is_dir(dir_path):
            return ["Directory doesn't exist."]
        files = get_files(dir_path)
        visible_files = list(filter(lambda file: not file.startswith("."), files))
        return visible_files


class NoHiddenFiles(Rule):
    """No hidden files allowed rule."""

    key = "noHiddenFiles"
    name = "No hidden files"

    def __repr__(self) -> str:
        """Return a representation of a NoHiddenFiles object."""
        return "NoHiddenFiles()"

    def check(self, directory: dict, dir_path: str) -> list:
        """Check that there are no hidden files in the given directory."""
        if not is_dir(dir_path):
            return ["Directory doesn't exist."]
        files = get_files(dir_path)
        hidden_files = list(filter(lambda file: file.startswith("."), files))
        return hidden_files


# All the defined rules
ALL_RULES = [
    NoUnknownDirectories(),
    NoHiddenDirectories(),
    NoVisibleFiles(),
    NoHiddenFiles(),
]


def check_rules(
    directory: dict,
    dir_path: str,
    rules_config: dict,
    print_checks: bool,
    prefix_print: str,
) -> bool:
    """Check all rules pass for a given directory.

    Keyword arguments:
    directory    -- The directory
    dir_path     -- The full expanded path of the directory
    rules_config -- The rules config
    print_checks -- Wether to print the rules checked or not
    prefix_print -- Prefix for the checks printed
    """
    all_rules_pass = True

    for rule in ALL_RULES:
        # Find if we should check the rule or not
        check_rule = directory.get(rule.key, rules_config[rule.key])

        if check_rule:
            rule_check = rule.check(directory, dir_path)
            rule_checked = len(rule_check) == 0
            all_rules_pass = all_rules_pass and rule_checked
            if rule_checked:
                reason = ""
            else:
                reason = f": {rule_check}"
        else:
            rule_checked = True
            reason = ": (rule set to false, check will always pass)"

        if print_checks:
            check_msg = (
                check.success(f"{rule.name}{reason}", print_checks)
                if rule_checked
                else check.failure(f"{rule.name}{reason}", print_checks)
            )
            print(f"{prefix_print}{check_msg}")

    return all_rules_pass
