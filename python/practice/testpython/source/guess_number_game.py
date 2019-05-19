import random

random_number = random.randint(1, 10)

guess_number = 0

while not guess_number == random_number:
    guess_number = int(input("Guessing number from 1 to 10: "))
    if guess_number > random_number:
        print("number is less than the your number")
    elif guess_number < random_number:
        print("number is greater than the your number")
    else:
        print("this is the number!")
