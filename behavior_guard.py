#!/usr/bin/env python3
"""Check user behavior against a keyword rule set."""

import sys

# Add blocked keywords here, for example: {"blocked keyword", "another keyword"}.
# Matching is case-sensitive; empty rules are ignored.
RULES: set[str] = set()


def check_behavior(behavior: str) -> str:
    """Check whether the behavior contains any configured keyword.

    Args:
        behavior: User behavior and relevant context to check.

    Returns:
        NO if any non-empty rule matches; otherwise YES.
    """
    if any(rule and rule in behavior for rule in RULES):
        return "NO"
    return "YES"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        behavior = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        behavior = sys.stdin.read()
    else:
        behavior = ""
    print(check_behavior(behavior))
