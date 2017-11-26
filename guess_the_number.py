# Guess The Number
from random import randint


def random_number():
    random_num = randint(1,10)
    return random_num


global random_num
random_num = random_number()


def check_number():
    if user_input.isdigit() and 1<= int(user_input) <= 10 :
        return True
    else:
        return False


def compare_numbers():
    if (random_num - int(user_input)) < 0 :
        print("Mehh, too big")
    elif (random_num - int(user_input)) > 0 :
        print("Too small brow!")
    elif (random_num - int(user_input)) == 0 :
        print("Gotcha!")
        quit()


def main_function():
    print ("A random number between 1 and 10 has been generated. What do you think this number is?")
    global user_input
    user_input = raw_input()

    if check_number():
        compare_numbers()
        main_function()
    else:
        print("Please enter a valid value!")
        main_function()


main_function()
