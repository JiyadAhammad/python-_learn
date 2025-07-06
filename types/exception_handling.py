## Exceprion Handling
"""
Exception handling used to handle error without terminate the program
Add multiple expect for a try
"""
try:
    10 / 0
    pass
except ZeroDivisionError as e:
    print("Zero division error -> ", e)
except:
    print("An exception occurred")


def name(a, b):
    if b == 0:
        raise ValueError("")  # raise is used to throw an error


try:
    10 / 0
    pass
except ZeroDivisionError as e:
    print("Zero division error -> ", e)
finally:  # Finally will execute if we hit error or not
    print("finally excete")

try:
    10 / 0
    pass
except ZeroDivisionError as e:
    print("Zero division error -> ", e)
else:  # else will execute only when no error occur
    print("finally excete")
