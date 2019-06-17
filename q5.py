# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.


class Employee(object):
    def __init__(self):
        self.name = ''

    def getname(self):
        self.name = input()

    def printname(self):
        print(self.name.upper())


emp1 = Employee()
emp1.getname()
emp1.printname()
