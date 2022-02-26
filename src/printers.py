# -*- coding: utf-8 -*-

"""Pretty printers."""

import style


def print_dir_name(name: str, prefix: str = "", check_msg: str = "") -> None:
    """Pretty-print directory name."""
    print(f"{prefix}{style.YELLOW}{style.BOLD}{name}{style.RESET}{check_msg}")


def print_dir_info(desc: str, path: str, prefix_info: str) -> None:
    """Pretty-print directory information."""
    # Print description
    print(f"{prefix_info}{style.MAGENTA}Desc:{style.RESET}", end=" ")
    print(f"{desc}")

    # Print path
    print(f"{prefix_info}{style.MAGENTA}Path:{style.RESET}", end=" ")
    print(f"{style.CYAN}{path}{style.RESET}")
