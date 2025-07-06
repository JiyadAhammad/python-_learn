## Dictionaries
"""
Key-value pairs
hashmap are ordered and modifiable
keys are immutable
duplicate key not allowed
keys are case sensitive ()
"""

data = {
    "name": "jiayd",
    "age": 25,
    "is_married": True,
}

dict(name="jiyad", age=25, is_married=True)

data["name"]  # Accessing value using key
data.get("hai")  # None Because not in map
data.get("hai", 0)  # if key not present then return 0
data["place"] = "Bathery"  # Add new key to map
data["age"] = 26  # update value in the map
data.popitem()  # Remove last key value pair
data.keys()  # Return list of  all keys
data.values()  # Return list of  all values
data.items()  # Return list of tuples  all items in map
sorted(data)  # return a sorted list of key
