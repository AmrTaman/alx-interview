#!/usr/bin/python3
"""
this is module
"""


def pascal_triangle(n):
    """
    iam here
    """
    top = [1]
    bottom = []
    all = []
    if n <= 0:
        return []
    all.append(top)
    while(n - 1):
        bottom.append(1)
        if len(top) > 1:
            for idx in range(len(top) - 1):
                bottom.append(top[idx] + top[idx + 1])
        bottom.append(1)
        all.append(bottom)
        top = bottom
        bottom = []
        n -= 1
    return all
