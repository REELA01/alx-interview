#!/usr/bin/python3
"""lockboxes task"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    tboxes = len(boxes)
    keyset = [0]
    counter = 0
    index = 0

    while index < len(keyset):
        setkey = keyset[index]
        for key in boxes[setkey]:
            if 0 < key < tboxes and key not in keyset:
                keyset.append(key)
                counter += 1
        index += 1

    return counter == tboxes - 1
