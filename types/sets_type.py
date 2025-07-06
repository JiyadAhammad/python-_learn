## Sets
"""
Doesn't allow duplicate value insets
Sets are unordered
"""

my_set = {1, 2, 3, 4, 1}  # return {1,2,3,4} ignore duplicates

my_list = [1, 2, 3, 4, 1, 2]
new_set = set(my_list)  # Convert the my_list into set

new_set[0]  # return error because of unordered

new_set.add(5)  # Add new element to set
new_set.remove(4)  # remove element from set
new_set.pop()  # remove last element

first_set = {1, 2, 3, 4}
second_set = {1, 2, 11, 12}

first_set.intersection(second_set)  # Return the common value in both set {1,2}
first_set & second_set  # another way of above #INTERSECTION

first_set.union(second_set)  # combaine the element in both and remove duplicates
first_set | second_set  # UNION

first_set.difference(second_set)  # Element which are in first but not second
first_set - second_set  # DIFFERENCE

# Elements which are present in either set but not in both
first_set.symmetric_difference(second_set)  # remove of intersection
# Set which contain all values in the second set
first_set.issubset(second_set)
# Second Set contain all values in first set
first_set.issuperset(second_set)
# Both sets need differnet elements
first_set.isdisjoint(second_set)
