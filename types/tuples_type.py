## Tuples
"""
Similar like list but tuples are immutable
list are created using [] but tuples are in ()
we can convert tuple into list -> then modify -> convert back to tuple
"""

my_tuple = (1, 2, 3)

my_tuple = list(my_tuple)  # Convert the tuple into list

my_tuple = tuple(my_tuple)  # Convert back to tuple from list


for ele in my_tuple:
    ele  # Looping through elements in tuple

my_tuple.index(1)  # return the idndex of value 1
my_tuple.count(1)  # Return number of occurrences of value.
