# Dice Rolling Simulator
from random import randint


def roll(sides=6):
    num_rolled = (randint(1,sides))
    return num_rolled


def main():
    sides = 6
    play = True
    while play == True:
        print ("The dice has been rolled and the result is:")
        print (roll())
        print ("Do you want to roll the dice again? (Y/N)")
        choice = raw_input()

        if choice == "Y":
            play = True
        elif choice == "N":
            print ("Thanks for playing!")
            play = False
        else:
            print("Please input a valid choice")
            play = False


main()
