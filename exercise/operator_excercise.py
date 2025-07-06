user_input = int(input("Enter access code"))

is_valid_code = user_input >= 100 and user_input <= 9999
is_member = user_input == 69 or user_input == 420 or user_input == 69420

is_grandted = is_valid_code or is_member

""" this 
if is_valid_code or is_member:
    print("Access Granted 😜")
else:
    print("Access Denied 🙅")

"""  # or

print("Access Granted 😜" * is_grandted + "Access Denied 🙅" * (not is_grandted))
