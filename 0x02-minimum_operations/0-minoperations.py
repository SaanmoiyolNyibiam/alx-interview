#!/usr/bin/python3
"""
--- This module answers the following question ---
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    This is a method that calculates the fewest number of operations
    needed to result in exactly n H characters in a file.
    """
    if n <= 1:
        return 0

    chars_in_file = 1
    total_operations = 0
    clip_board_chars = 0

    while chars_in_file < n:
        if n % chars_in_file == 0:
            clip_board_chars += chars_in_file
            chars_in_file += chars_in_file
            total_operations += 2
        else:
            chars_in_file += clip_board_chars
            total_operations += 1

    return total_operations
