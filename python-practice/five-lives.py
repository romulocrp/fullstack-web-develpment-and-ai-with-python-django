import random

num = random.randint(1, 100)
lives = 5

guess = int(input("Guess a number between 1 and 100, you have 5 tries:\n"))

while lives != 1:
    if guess > num:
        lives -= 1
        print(f"The number is lower than your guess. Tries left {lives}.")
        guess = int(input("Try again:\n"))
    elif guess < num:
        lives -= 1
        print(f"The number is higher than your guess. Tries left {lives}.")
        guess = int(input("Try again:\n"))
    elif guess == num:
        break

if guess != num:
    print(f"Game over, the number was {num}")    
else:
    print(f"Congratulations you guessed {num}!")