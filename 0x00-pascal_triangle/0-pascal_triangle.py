#!/usr/bin/env python3
"""This a module that has a function that creates a pascal triangle"""


def pascal_triangle(n):
    """This is a function that creates
        a pascal triangle"""
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j in (0, i):
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle
