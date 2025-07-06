# Accept user input budget
# Get user is vegitaerian or not
# if vegitaeraian add Chiken breast else tofu
# add rest according to the budget

budget = int(input("Enter user budget max($30)"))
veg_or_not = input("Veg or non-veg (1 -> veg , 2 -> non-veg)")
if veg_or_not == "1":
    is_veg = True
else:
    is_veg = False

grocery_list = []
if is_veg:
    grocery_list.append("Tofu")
else:
    grocery_list.append("Chiken breast")

if budget < 30:
    if budget >= 5:
        grocery_list.append("Broccoli")
        budget -= 5
    if budget >= 10:
        grocery_list.append("Carrotes")
        budget -= 10
    if budget >= 15:
        grocery_list.append("Bell peppers")
        budget -= 15
print(grocery_list)
