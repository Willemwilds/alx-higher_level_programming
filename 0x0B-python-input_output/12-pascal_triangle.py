#!/usr/bin/python3
"""
This module defines pascal_triangle(n) function.
"""


def pascal_triangle(n):
    """
    This function returns the Pascal triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]

        for num in range(len(tri) - 1):
            tmp.append(tri[num] + tri[num + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
