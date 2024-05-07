#OOP_Exercise_5__Define_a_property_that_must_have_the_same_value_for_every_class_instance__object_.py

# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# Use the following code for this exercise.
class Vehicle:
    color = "white"

    def __init__(self, name, max_speed, mileage):     
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def __str__(self):
        return f"Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus("School Volvo", 180, 12)
car = Car("Audi Q5", 240, 18)

print(bus)
print(car)


# Expected Output:

# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

# Refer: Class Variable in Python

