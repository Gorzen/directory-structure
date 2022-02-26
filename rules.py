# -*- coding: utf-8 -*-

"""Defines all the different rules for the directory structure."""

from abc import ABC, abstractmethod

class Rule(ABC):
    """A rule for the directory structure"""

    key: str

    def __repr__(self) -> str:
        "Rule()"

    @abstractmethod
    def check(self, path: str) -> bool:
        """Check that rule is valid for the directory located at path"""
        return NotImplemented


class NoUnknownDirectories(Rule):
    """No unknown (not declared in the directory structure) directories allowed rule."""

    key = 'noUnknownDirectories'

    def __repr__(self) -> str:
        "NoUnknownDirectories()"

    def check(self, path: str) -> bool:
        return True


class NoVisibleFiles(Rule):
    """No visible files allowed rule."""

    key = 'noVisibleFiles'

    def __repr__(self) -> str:
        "NoVisibleFiles()"

    def check(self, path: str) -> bool:
        return True


class NoHiddenFiles(Rule):
    """No hidden files allowed rule."""

    key = 'noHiddenFiles'

    def __repr__(self) -> str:
        "NoHiddenFiles()"

    def check(self, path: str) -> bool:
        return True


# All the defined rules
ALL_RULES = [NoUnknownDirectories(), NoVisibleFiles(), NoHiddenFiles()]
