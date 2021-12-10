"""This is the main function"""
from lib.get_num import get_num
from lib.multiplier import multiplier


def main():
    """
    Main function

    """
    num = get_num()
    print(multiplier(num))


if __name__ == "__main__":
    main()
