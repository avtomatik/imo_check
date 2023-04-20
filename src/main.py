#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:46:18 2023

@author: green-machine
"""


def is_valid_imo(imo: str) -> bool:
    """
    Checks If Valid IMO Number

    Parameters
    ----------
    imo : str
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    return sum(
        map(lambda _: _[0] * int(_[1]), enumerate(imo[::-1][1:], start=2))
    ) % 10 == int(imo[-1])


if __name__ == '__main__':
    imo = ""
    while len(imo) != 7:
        imo = input("Input IMO, 7-Digit Number, Like 9000003: ")

    print(is_valid_imo(imo))
