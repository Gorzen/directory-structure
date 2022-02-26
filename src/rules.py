# -*- coding: utf-8 -*-

"""Defines all the different rules for the directory structure."""

from abc import ABC, abstractmethod


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
