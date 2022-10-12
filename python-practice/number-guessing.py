import random

num = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100:\n"))

while guess != num:
    if guess > num:
        print("The number is lower than your guess.")
        guess = int(input("Try again:\n"))
    elif guess < num:
        print("The number is higher than your guess.")
        guess = int(input("Try again:\n"))

print(f"Congratulations you guessed {num}!")