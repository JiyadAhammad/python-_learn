## Classes
"""
Python is an object oriented programming language
it contains objects and behavior
Everything in python are objects -> list , class , string etc...
"""


class MyClass:
    # initalize the state of the object
    def __init__(self, name, age):  # Object initalize like constructor
        self.name = name  # instance variable
        self.age = age
        self.sex = "Male"  # Default value

    def hai(self):  # Self refernce the current object
        print("hy from class")

    # pass  # pass used for intentaion no error will give if we not use any logic


obj = MyClass("Jiyad", 25)  # Object of class MyClass
obj1 = MyClass(name="akhil", age=23)  # named parameter

obj.name  # get name from class
obj.hai()  # calling function using object
obj1.name = "akhil"  # create a value of akhil to name in new object


# __init__ method
"""
Magic method
Start and end with double underscore -> __*__
Class by python itself 
"""
# eg
num = 10
num = num.__add__(20)  # Output will be 30 -> 10 + 20
