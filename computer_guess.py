def main():
    maxi = int(raw_input("Choose the max number possible \t"))
    print('Choose a number in your head between zero and that range \n')

    guessed = False
    mini = 0
    guess = ((maxi + mini)/ 2)

    while not guessed:
        print('The computer thinks it is: ' + str(guess))
        choice = raw_input('Is it your number? (Y / N)').upper()

        if choice == 'Y':
            print('GOTCHA!')
            guessed = True
        elif choice == 'N':
            choice2 = raw_input('Is it greater or smaller? (G / S)').upper()

            if choice2 == 'G':
                mini = guess
            elif choice2 == 'S':
                maxi = guess

            guess = (maxi + mini) / 2
        else:
            print('Input a valice choice')


main()
