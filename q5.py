# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.fullname = name + surname

    def getfullname(self):
        self.fullname = input()

    def printfullname(self):
        print(self.name + self.surname.upper())
