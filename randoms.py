import random


def get_random_number():
    return random.randint(1, 10)

secret_number = get_random_number()

guesses = 3


while True:
    number = int(input('Enter a number: '))
    if number == secret_number:
        print('goooooooooood')
        break
    elif number > secret_number:
        print('is smaller')
        guesses -= 1
    elif number < secret_number:
        print('is bigger')
        guesses -= 1
    if guesses == 0:
        print('LOST')
        break

    

