class BasicCalculator():

    def __int__(self, name, a, b, c):

        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def user_input_values(self):
        self.name = input("What's your name?\n")
        self.a, self.b, self.c = [float(x) for x in input("Input your numbers, separated by space:\n").split()]
        return self.name, self.a, self.b, self.c

    def print_results(self):
        result = (self.a + self.b) * self.c
        return f"Your name is: {self.name}\n\
The numbers you inputed are: {self.a:.2f}, {self.b:.2f} and, {self.c:.2f}\n\
The result is: {result:.2f}"

if __name__=="__main__":
    bc = BasicCalculator()
    bc.user_input_values()
    print(bc.print_results())