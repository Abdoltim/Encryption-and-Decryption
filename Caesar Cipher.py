# @Author: Mohamed Radwan
# @Date: 2018-01-17
# Rotates a list of characters based on the inputed rotate number
# to add an easy way for encryption

import string
import collections


def caesar(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(
        str.maketrans(string.ascii_lowercase, lower))


