#!/usr/bin/python3
"""
this is module
"""


def canUnlockAll(boxes):
    """
    iam here
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    queue = [0]

    while queue:
        target_box = queue.pop(0)
        for key in boxes[target_box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
    return all(unlocked)
