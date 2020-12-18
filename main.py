import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the number between 1 and {x}:"))
        if guess < random_number:
            print('sorry too low')
        elif guess > random_number:
            print("sorry too high")
    print(f'you have guessed the number {random_number}')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} too high,too low,or correct").lower()
        if feedback == 'h':
            high = guess-1
        if feedback == 'l':
            low = guess+1
    print(f'the computer guessed {guess} correctly')


computer_guess(10)
