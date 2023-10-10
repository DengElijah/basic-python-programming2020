import random

def guess(X):

    random_number = random.randint(1, X)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {X}:'))
        if guess < random_number:
            print('sorry,guess again .too low.')
        elif guess > random_number:
            print('sorry, guess again .too high')

            print ('yah , congrats you have guessed the number{random_number} correctly!!')
        
        guess(10)


