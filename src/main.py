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
    check_sum = sum(
        [
            _ * int(num) for _, num in enumerate(imo[::-1], start=1) if _ != 1
        ]
    )
    return check_sum % 10 == int(imo[-1])


if __name__ == '__main__':
    imo = "9000003"

    print(is_valid_imo(imo))
