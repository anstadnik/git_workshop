def get_num():
    """
    This function asks for an input

    """
    while 42:
        num = input("Please input your number: ")
        try:
            num = int(num)
            return num
        except ValueError as e:
            print(f"Wrong input: {e}")
            print()
