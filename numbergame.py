

import random


def main():
    ra = random.randint(1, 100)

    while True:
        index = int(input("Enter a number between 1 and 100: ")) - 1
        if index < ra:
            print("Too low!")
        elif index > ra:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break


def child(main):
    pass


main()
