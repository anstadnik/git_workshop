"""This module contains logic for interaction with the user"""

def get_num():
    """
    This function asks for an input

    """
    while 42:
        num = input("Please input your number: ")
        try:
            num = int(num)
            return num
        except ValueError as err:
            print(f"Wrong input: {err}")
            print()
