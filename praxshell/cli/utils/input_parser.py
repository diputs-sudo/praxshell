"""
Input parsing for Praxshell.
Currently minimal — just split command + args.
"""

import shlex

def parse_command(line: str) -> tuple[str, str]:
    words = shlex.split(line)
    if not words:
        return "", ""
    return words[0], " ".join(words[1:])
