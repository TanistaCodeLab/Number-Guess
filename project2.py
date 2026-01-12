import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Enter a number between 1 to {x}:'))
        if guess < random_number:
            print('incorrect guess, its too low')
        elif guess > random_number:
            print('incorrect guess, its too high')

    print(f'Congrats! Your guess {random_number} is absolutely correct')
guess(10)  
