annual_revenue = int(input("Enter your annual revenue"))
total_employees = int(input("Enter total employees"))
is_valid_duration = input("Business operate atlest 2 year type (yes or no)")

if annual_revenue < 50000:
    print("Annual revenue must be 50000")
elif total_employees < 3:
    print("Employees atlest 3")
elif is_valid_duration != "yes":
    print("Atlest 2 year buesiness opearte")
else:
    print("Eligible for laon")
