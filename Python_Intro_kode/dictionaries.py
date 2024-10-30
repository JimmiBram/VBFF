# 1. Creating a Dictionary

# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with initial values
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 2. Accessing Values

# Accessing a value using a key
print(my_dict["name"])  # Output: Alice

# Using .get() to access a value (returns None if the key doesn't exist)
print(my_dict.get("age"))  # Output: 25
print(my_dict.get("country"))  # Output: None

# 3. Adding or Updating Key-Value Pairs

# Adding a new key-value pair
my_dict["country"] = "USA"

# Updating an existing key-value pair
my_dict["age"] = 26

# 4. Removing Key-Value Pairs

# Using del to remove a key-value pair
del my_dict["city"]

# Using .pop() to remove a key-value pair and get its value
age = my_dict.pop("age")
print(age)  # Output: 26

# Using .popitem() to remove the last key-value pair (Python 3.7+)
last_item = my_dict.popitem()
print(last_item)

# 5. Looping Through a Dictionary

# Looping through keys
for key in my_dict:
    print(key)

# Looping through values
for value in my_dict.values():
    print(value)

# Looping through both keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 6. Checking if a Key Exists

if "name" in my_dict:
    print("Name exists in the dictionary")

# 7. Merging Dictionaries

# Using the update() method
other_dict = {"hobby": "painting", "city": "San Francisco"}
my_dict.update(other_dict)

# 8. Dictionary Comprehension

# Creating a new dictionary by transforming an existing dictionary
squared_numbers = {num: num ** 2 for num in range(1, 6)}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#Loading and storing

import json

# Sample dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Saving (storing) the dictionary to a JSON file
with open("my_dict.json", "w") as file:
    json.dump(my_dict, file)

# Loading the dictionary back from the JSON file
with open("my_dict.json", "r") as file:
    loaded_dict = json.load(file)

print(loaded_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}