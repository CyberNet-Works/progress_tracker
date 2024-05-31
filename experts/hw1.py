# hw1
# 16:17, 16:30
# Print a Message:
# Write a program that prints "Hello, World!" to the console.
print("Hello, World!")

# Integer and Float Variables:
# Create two variables, an integer x and a float y, and initialize them with values 5 and 10.5 respectively. Print both variables.
x = 5
y = 10.5
print(x)
print(y)

# Basic Arithmetic:
# Take two integers as input from the user. Print the sum, difference, product, and quotient of these numbers.

user_input1 = int(input("Enter integer"))
user_input2 = int(input("Enter integer2"))

_sum = user_input1 + user_input2
_difference = user_input1 - user_input2
_product = user_input1 * user_input2
_quotient = user_input1 / user_input2

print(_sum)
print(_difference)
print(_product)
print(_quotient)


# Combining Strings and Numbers:
# Create a variable containing your age as an integer. Then, print a message saying "I am [age] years old" by using the variable in the print statement.

_age = 44
print(f"I am {_age} years old")


# Calculating Area:
# Write a program that takes the radius of a circle (as a float) from the user and calculates the area using the formula 

import math

def area(_radius):
   return _radius * _radius * math.pi

if __name__ == "__main__":
    _radius_input = float(input("Enter Radius: \n"))
    result = area(_radius_input)
    print(result)
   

# Swapping Two Variables:
# Create two variables, a and b, with integer values. Write a program that swaps the values of these variables without using a third variable. Print the values of a and b before and after swapping.

a = 1
b = 2
print(a)
print(b)

a, b = b, a
