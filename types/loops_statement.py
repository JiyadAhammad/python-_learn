## Loops
"""
Block of code using repeatedly
    -> While loop
    -> For loop
    -> break used to exit loop
    -> Continue skip the loop
"""
# while
num = 0

while num < 6:
    # print(num)
    num += 1
# else:
#     print("While endted")

# for

# range(0, 5, 3)
# range(5)  # 0 to 4
# range(1, 5)  # 1 to 4
# range(1, 5, 2)  # 1 to 5 skip 2 op=> 1,3
# range(5, 0)  # 5 to 1 reverse order

for i in range(1, 4):
    i
    # print(i)
# else:
#     print("for loop done")

#  if we add break in for lopp then else will not excecuted

name = "jiyad"

for i, char in enumerate(name):
    i
    # print(i, char)


# For vs While

# List comprehension

names = ["jiyad", "jack", "jhon", "arun", "akhil"]
names_with_j = [i for i in names if "a" in i.lower()]

print(names_with_j)
