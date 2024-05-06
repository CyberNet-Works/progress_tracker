#Create_a_child_class_Bus_that_will_inherit_all_of_the_variables_and_methods_of_the_Vehicle_class.py
#expected_output: Vehicle Name: School Volvo Speed: 180 Mileage: 12


class Vehicle:
    def __init__ (self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __str__(self):
        return f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}"
    
class Bus(Vehicle):
    pass

Volvo = Vehicle("School Volvo", 180, 12)
print(Volvo)