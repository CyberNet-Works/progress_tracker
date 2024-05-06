#OOP_Exercise_4:_Class_Inheritance.py

# Given:
# Create a Bus class that inherits from the Vehicle class. 
# Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class.

# Expected Output:
# The seating capacity of a bus is 50 passengers
# Refer:

# Inheritance in Python
# Polymorphism in Python


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

School_bus = Bus("Bus", 200, 12)
print(School_bus.seating_capacity())
    

