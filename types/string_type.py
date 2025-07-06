## String data type
"""
Collection of character enclosed in single or double quotes
String are immutable (Value cannot be changed once created)
"""

name = "jiyad"

a = "first"
b = "Second"
c = "thrid"
# String concatenate
full_data = a + " " + b + " " + c

# user_data = input("What's your name")
user_data = "Jiyad"
input_length = len(user_data)
user_data[-2]  # Taken from Back -1 , -2 , -3
user_data[1:4]  # Range from 1-4
user_data[:3]  # Range from 0-3
user_data[3:]  # Range from 3-endIndex
user_data[:]  # Range from Start - End

user_data[::2]  # Range from first to last but jum 2 in jiyad -> jyd

user_data[::-1]  # Reverse order (print the string in reverse)

# String formatting
name = "jiyad"
age = 25

# name print in the bracket with forward order
formatted_string = "my name is {} im {} age year old".format(name, age)
# name print in the bracket with key argument
formatted_string1 = "my name is {na} im {ag} age year old".format(na=name, ag=age)
# anme print with key argument but the lenght take 10 spacd
# if character then 5 space added to make it 10 charcter long
# if more than 10 character it ignore spacing and prit whole
formatted_string1 = "my name is {na:10} im {ag} age year old".format(na=name, ag=age)
# We can add < = space before the value
# We can add > = space After the value
# We can add ^ = value will in center follwed before and after with equal space
formatted_string1 = "my name is {na:<10} im {ag} age year old".format(na=name, ag=age)
# Simple way to add formatting string = fString
formatted_string1 = f"my name is {name} im {age} age year old"

pi = 3.14159
formatted_pi = f"Value of pi {pi:.2f}"  # toStringAsFixed(2)

# escape sequence
# \, \n , \t , \\  -> Some examples

# String methods
"jiyad".upper()  # Conver to upper case
"jiyad".lower()  # Conver to lower case
"jiyad".capitalize()  # Conver to firest letter upper case

my_name = "jiyad ahammad"
my_name = my_name.title()  # Capitalize all first charcter after space
my_name = " jiyad ahammad.  ".strip()  # Remove leading and trailing space  removed
my_name.replace("a", "*")  # Remove all a with *

name.count("a")  # Count the number of a and return the length

"jiy" in name  # check the jiy in the string name if exist reutrn true
"jiy" not in name  # Check jiy is not present in the string

name * 3  # it return the name 3 times -> jiyadjiyadjiyad
