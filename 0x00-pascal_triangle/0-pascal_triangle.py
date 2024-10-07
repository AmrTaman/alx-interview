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
    if n <= 0:
        return []
    print(top)
    while(n):
        bottom.append(1)
        if len(top) > 1:
            for idx in range(len(top) - 1):
                bottom.append(top[idx] + top[idx + 1])
        bottom.append(1)
        print("[{}]".format(",".join([str(x) for x in bottom])))
        top = bottom
        bottom = []
        n -= 1
