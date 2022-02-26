# -*- coding: utf-8 -*-

"""Defines all the different rules for the directory structure."""

from abc import ABC, abstractmethod

class Rule(ABC):
    """A rule for the directory structure"""

    def __repr__(self):
        "Rule()"

    @abstractmethod
    def check(self, path):
        """Check that rule is valid for the directory located at path"""
        return NotImplemented


class NoUnknownDirectories(Rule):
    """No unknown (not declared in the directory structure) directories allowed rule."""

    key = 'noUnknownDirectories'

    def __repr__(self):
        "NoUnknownDirectories()"

    def check(self, path):
        return ''


class NoVisibleFiles(Rule):
    """No visible files allowed rule."""

    key = 'noVisibleFiles'

    def __repr__(self):
        "NoVisibleFiles()"

    def check(self, path):
        return ''


class NoHiddenFiles(Rule):
    """No hidden files allowed rule."""

    key = 'noHiddenFiles'

    def __repr__(self):
        "NoHiddenFiles()"

    def check(self, path):
        return ''


allRules = [NoUnknownDirectories, NoVisibleFiles, NoHiddenFiles]
