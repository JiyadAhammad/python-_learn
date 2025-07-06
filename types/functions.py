## Functions
"""
Block of code that do a specific task
declare function first then called it else name error
"""


def new_function():
    print("hello fucntion called")
    pass


name = ""


def a_function(name):  # parameter
    name


def b_function(name, age):  # parameter
    name


def c_function(name, age, /):  # / Accept only posotional argument
    name


# name is posotional argument and age is named or postinal
def d_function(name, /, age):
    name


def e_function(*, name, age):  # Accept only named argument
    name


# name is posotional or named argument and age is  only
def f_function(name, *, age):
    name


# a,b -> Positional , c,d -> named
def g_function(a, b, /, *, c, d):
    name


def h_function(a, b=10):  # Accept default value
    name


def i_function(*a):  # accpet multiple value to a
    name


def j_function(b, *a):  # b accept a value and a accpet multiple value
    name


def k_function(**a):  # accpet multiple value to with named paramameter
    name


def l_function(a):  # return function
    name
    return a


new_function()
a_function("jiyad")  # argument (Positional)
# if we add named parameter then both will namedparmeter
b_function(age=20, name="jiyad")
c_function(20, "jiyad")  # positional argument
d_function("jiyad", age=20)  # Mix argument
e_function(name="jiyad", age=20)  # only named argument
f_function("jiyad", age=20)  # age should be named
g_function("a", "b", c="c", d="d")  # a,b -> Positional , c,d -> named
h_function("jiyad")  # b is default
i_function("a", "b", "c")  # accpet multiple values to a in form of tuple
j_function("a", "b", "c")  # First value as postional and rest all value to a
# pass multiple value to with named paramameter return a dictionary
k_function(a="a", b="b", c="c")
l_function(a="a")  # Give result here, What return there


# Scope
"""
local variable and global variable
Variable create inside the function are not get outside 

varibale in for or if will get out side

LEGB -> local , enclosing , global , build-in
"""

x = 100


def update():
    # mentioned that we are using global x variable to reassign te variable
    # If global is not mentioned then it will be like create a new local variable
    # if x is not created then it will create a global scope x variable
    global x
    x = 200


update()
