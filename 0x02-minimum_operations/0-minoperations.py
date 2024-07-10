#!/usr/bin/python3
"""minimum Operations challenge"""


def minOperations(n):
    """
    counts the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Return:
        Integer : if n or return 0
    """
    pasted_ch = 1
    clipboard = 0
    count = 0

    while pasted_ch < n:
        if clipboard == 0:
            clipboard = pasted_ch
            count += 1
        if pasted_ch == 1:
            pasted_ch += clipboard
            count += 1
            continue

        remaining = n - pasted_ch
        if remaining < clipboard:
            return 0
        if remaining % pasted_ch != 0:
            pasted_ch += clipboard
            count += 1
        else:
            clipboard = pasted_ch
            pasted_ch += clipboard
            count += 2

    if pasted_ch == n:
        return count
    else:
        return 0
