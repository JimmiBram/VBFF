# 30 Fundamental Python Functionalities with Examples and Practice Tasks

# 1. Print Statements
print("Hello, World!")
# Task: Print your name to the console.

# 2. Comments
# This is a single-line comment
"""
This is a
multi-line comment
"""
# Task: Write a single-line comment above a line of code explaining what it does.

# 3. Variables
x = 10
name = "Alice"
# Task: Create a variable to store your age and print it.

# 4. Data Types
age = 25          # int
price = 19.99     # float
is_student = True # bool
name = "John"     # str
# Task: Create a variable for each data type (int, float, str, bool) and print them.

# 5. Type Conversion
number = int("5")         # converts string to integer
height = float(5)         # converts integer to float
text = str(123)           # converts integer to string
# Task: Convert a string to an integer, add 10 to it, and print the result.

# 6. Operators
x = 10 + 5       # addition
y = 10 > 5       # comparison, returns True
# Task: Use the `*` operator to multiply two numbers and print the result.

# 7. Input
name = input("Enter your name: ")
print("Hello, " + name)
# Task: Ask the user for their favorite color and print a message that includes their answer.

# 8. Conditional Statements
age = 18
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
# Task: Create a program that checks if a number is positive, negative, or zero and prints the result.

# 9. Loops
for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1
# Task: Write a loop that prints each character in the string "Python".

# 10. Break and Continue
for i in range(10):
    if i == 5:
        break   # stops the loop when i is 5
    print(i)

for i in range(10):
    if i == 5:
        continue  # skips the rest of the code when i is 5
    print(i)
# Task: Write a loop that prints numbers from 1 to 10, but skips the number 7.

# 11. Functions
def greet():
    print("Hello!")

greet()
# Task: Create a function that takes a name as input and prints a greeting with that name.

# 12. Return Statement
def add(x, y):
    return x + y

result = add(3, 4)
print(result)
# Task: Create a function that returns the square of a number.

# 13. Lambda Functions
square = lambda x: x * x
print(square(5))
# Task: Create a lambda function that adds 5 to a given number.

# 14. Lists
my_list = [1, 2, 3, 4]
print(my_list[0])
# Task: Create a list with 5 items and print the third item.

# 15. List Comprehension
squares = [x * x for x in range(5)]
print(squares)
# Task: Use list comprehension to create a list of even numbers from 0 to 10.

# 16. Tuples
my_tuple = (1, 2, 3)
print(my_tuple[1])
# Task: Create a tuple with three items and print the last item.

# 17. Dictionaries
person = {"name": "Alice", "age": 25}
print(person["name"])
# Task: Create a dictionary with keys "city" and "country" and print each value.

# 18. Sets
my_set = {1, 2, 3, 2}
print(my_set)  # duplicates are removed
# Task: Create a set with the numbers 1, 2, 2, 3, and 4, and print the set.

# 19. Indexing and Slicing
text = "Hello"
print(text[1])    # e
print(text[1:4])  # ell
# Task: Print the last 3 characters of the string "Programming".

# 20. String Manipulation
message = " Hello World "
print(message.strip().upper())  # "HELLO WORLD"
# Task: Take a string with spaces at the beginning and end, remove the spaces, and make it lowercase.

# 21. String Formatting
name = "Alice"
print(f"Hello, {name}!")
# Task: Format a string to include a user's age, e.g., "You are 21 years old."

# 22. Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
# Task: Write a try-except block to catch a `ValueError` when converting a non-numeric string to an integer.

# 23. Modules and Imports
import math
print(math.sqrt(16))  # 4.0
# Task: Use the `random` module to print a random number between 1 and 100.

# 24. File Handling
with open("sample.txt", "w") as file:
    file.write("Hello, file!")
# Task: Write a program that reads and prints the contents of a text file.

# 25. Classes and Objects
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()
# Task: Create a class `Car` with a method that prints "Vroom!". Create an instance and call the method.

# 26. Inheritance
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

my_dog = Dog()
my_dog.sound()
# Task: Create a subclass `Cat` that inherits from `Animal` and overrides the `sound` method with "Meow!".

# 27. List Methods
numbers = [1, 2, 3]
numbers.append(4)     # adds 4 at the end
numbers.remove(2)     # removes 2
print(numbers)
# Task: Use `pop()` to remove the last item from a list of numbers and print the result.

# 28. Dictionary Methods
person = {"name": "Alice", "age": 25}
print(person.keys())   # dict_keys(['name', 'age'])
print(person.values()) # dict_values(['Alice', 25])
# Task: Use `.get
