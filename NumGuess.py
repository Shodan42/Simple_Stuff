import random
import sys

# Generates a random number between 1 -100


def random_number():

    return random.randint(1, 100)


# Check that guess is a non zero positive int
def guess():
    while True:
        try:
            num_guess = int(input('What is your guess? '))
            if num_guess <= 0:
                print('Non zero positive numbers only please')
                continue
            return num_guess
        except ValueError:
            print('That is not a number, try again ')

# Check that username is valid str


def username():

    while True:

        try:
            name = input('What is your name? ')

            if name.isnumeric():
                print('That does not seem like a name try again')
                continue
            else:
                return name
        except ValueError:
            print('That does not seem like a name try again')

# Checks if you want to play the game. Exits program if not


def play(name):

    acceptable = ['yes', 'y']
    unacceptable = ['no', 'n']
    while True:

        play_game = input(f'Hello {name} do you want to play a game')

        if play_game.isdigit():
            print('I need a Yes or No try again')
            continue
        elif play_game.lower() in acceptable:
            return play_game
        elif play_game.lower() in unacceptable:
            print('Fine, I did not want to play with you anyways Bye Loser =P')
            sys.exit()
        else:
            print('that was weird try again')


def game(name):
    brain = random_number()
    play(name)

    while True:

            print(f'Okay, {name} im thinking of a number between 1-100')

            for x in range(1, 11):
                print(f'you have {11-x} guesses left')
                var_guess = guess()
                if brain > var_guess:
                    print(f'{var_guess} is too low try again')
                    continue
                elif brain < var_guess:
                    print(f'{var_guess} is too high try again')
                else:
                    print(f'Only took you {x} guesses')
                    return None

            print("Better luck next time")
            break


game(username())