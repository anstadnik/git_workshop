"""This module contains a multiplication logic"""
import doctest

def multiplier(num: int) -> int:
    """
    This function returns a number, multiplied by 2

    :param n int: n
    :rtype int: n * 2

    >>> multiplier(2)
    4
    >>> multiplier(3)
    6
    """
    return num * 2

def main():
    """
    Main function, needed for doctest

    """
    doctest.testmod(raise_on_error=True)

if __name__ == "__main__":
    main()
