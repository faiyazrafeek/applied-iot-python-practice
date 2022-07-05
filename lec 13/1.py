class Electrical:
    def __init__(self, name, use):
        print('Object created')
        self.name = name
        self.use = use

    def printDetails(self):
        print("The details of Electrical\n")
        print("Name: " + self.name)
        print("Use: " + self.use)


ob1 = Electrical('bulb','light')

ob1.printDetails()



class A:
    def __init__(self):
        print('Object created')

    def fun(self):
        print('Fun method of Class A')

from a import *
from c import *

f1()
f2()
f3()