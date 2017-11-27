import random


def get_word() :
    words = ['computer', 'table', 'building', 'medecine', 'hungry', 'dinosaur', 'internship', 'death']
    return random.choice(words).upper()


def check(word, guesses, guess) :
    status = ''
    matches = 0

    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'
        if letter == guess:
            matches +=1

    if matches > 1:
        print('Yes! The word contains ', matches, '""' + guess + '""' + 's')
    elif matches ==1:
        print('Yes! The word contains the letter ' + guess)
    else:
        print('Sorry. The word doesnt contain the letter ' + guess)

    return status


def main() :
    word = get_word()
    guesses = []
    guessed = False
    print ('The word contains ' + str(len(word)) + ' letters.')

    while not guessed:
        text = ('Please enter one letter or a {} letter word \n' .format(len(word)))
        guess = raw_input(text).upper()

        if guess in guesses:
            print('You already guessed ' + guess + ' !')
        elif len(guess) == len(word) :
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print ('Sorry, that is incorrect.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess)

            if result == word:
                guessed = True
            else:
                print(result)
        else:
            print('Invalid entry.')

    print('Yes the word is ' + word + '! You got it in ' + str(len(guesses)) + ' tries. Thats okay!')


main()
