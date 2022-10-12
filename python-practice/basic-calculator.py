name = input("What's your name?\n")

a, b, c = [float(x) for x in input("Input your numbers, separated by space:\n").split()]

result = (a + b) * c

print(f"Your name is: {name}\n\
The numbers you inputed are: {a}, {b} and, {c}\n\
The result is: {result}")