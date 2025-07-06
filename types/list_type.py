## Lists
"""
Store multiple value in a single variable
    new_data = [a,b,c,d]
List can store elements of multiple data types
    mix_data = ['a',2,3.5,a+bj]
List are mutable we can change the items inside the list
"""

a = [1, 2, 3, 4]

# Unpacking of elements
a1, a2, a3, a4 = a  # Assigne each number in list to each variable
# lenght should match with the list elements

a1, *a2 = a  # a1 take the first character and then rest will assign to a2
# a1 take the first character and then rest will assign to a2 and a3 takes last element
a1, *a2, a3 = a

length = len(a)  # Length of the list
# len(a[0])  # length of first element

a[-1] = 5  # change the last element into 5 -> 4 = 5

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
dumy = list1 + list2  # Merge two array into single array
dumy = dumy * 2  # dummy list printed 2 times

# list methods
name = [1, 2, 3]
name.append(5)  # Add new element into list
name.insert(0, 6)  # insert element into mentioed position
name.pop()  # remove last element
name.remove(1)  # Remove the mentioned item from list
name.index(2)  # Return the index of the value
name.sort()  # Sort the list
sorted(name)  # sort and return new list

1 in name  # return True if 1 present in list
",".join(name)  # return a String which the list with a ,
name.clear()  # remove all the elements in the list
