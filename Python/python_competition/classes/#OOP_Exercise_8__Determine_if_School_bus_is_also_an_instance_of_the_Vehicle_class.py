#OOP_Exercise_8__Determine_if_School_bus_is_also_an_instance_of_the_Vehicle_class.py       
# Given:

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus, Vehicle))
