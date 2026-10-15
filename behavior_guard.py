#!/usr/bin/env python3
"""Provide the initial behavior-checking stub and standalone CLI."""


def check_behavior(behavior: str) -> str:
    """Return the fixed test result regardless of the supplied behavior.

    Args:
        behavior: Behavior description, ignored by this initial test version.

    Returns:
        The literal string YES.
    """
    return "YES"


if __name__ == "__main__":
    print("YES")
