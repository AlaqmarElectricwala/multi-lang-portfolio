import sys
from pyfiglet import Figlet
import random

figlet = Figlet()


def main():
    # Checking for correct number of arguments
    if len(sys.argv) == 1 or len(sys.argv) == 3:

        if len(sys.argv) == 3:
            # Checking for correct arguments
            check_arg(sys.argv[1], sys.argv[2])

        user_input = input("Input: ")

        # If no.of arguments is 0
        if len(sys.argv) == 1:
            f = Figlet(random.choice(figlet.getFonts()))
            print(f.renderText(user_input))

        # If no.of arguments is 2
        elif len(sys.argv) == 3:
            f = Figlet(sys.argv[2])
            print(f.renderText(user_input))

    else:
        sys.exit("Invalid usage")


# Checking for correct arguments
def check_arg(a, b):

    # Checking first arugment
    if a != '-f' and a != '--font':
        sys.exit("Incorrect Arguments")
    # Checking second argument
    if b not in figlet.getFonts():
        sys.exit("Incorrecct Arguments")


if __name__ == "__main__":
    main()
