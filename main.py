import random

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0

    while randomNumber != guess :
        guess = int(input(f'Guess a Number between 1 and {x} :'))
        if randomNumber > guess:
            print("Hey Sorry, Guess again, To High")
        elif randomNumber < guess:
            print("Hey Sorry, Guess again, To Low")

    print(f"Hey... congrats You have guessed the Number {randomNumber} correctly!!")

numberRange = int(input("Enter Maximum Range of guess : "))
guess(numberRange)
