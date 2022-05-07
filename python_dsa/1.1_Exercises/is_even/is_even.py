import sys


def is_even(n: int or float) -> bool:
    """
    ## Takes in a numeric arg and determines if it is even or not
    
    Args:
        n: int or float

    Returns:
        bool    
    """
    # sanitize input
    try:
        if float(n) != int(n):
            return False
        n = int(n)
    except ValueError:
        print("Invalid Entry")
        sys.exit()

    starting = n

    n = abs(n)

    while True:
        if n == 0:
            return True
        elif n > 0:
            n -= 2
        else:
            return False


if __name__ == "__main__":

    try:
        x = sys.argv[1]
    except IndexError:
        print("No values passed in.")
        sys.exit()

    is_even(x)
