#Classes_create_vehicle_class_instance_attributes_max_speed_and_mileage
class Vehicle:
    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __str__(self):
        return f"Maximum speed:{self.max_speed}\nMileage:{self.mileage}"
    
mitsubishi_spacestar = Vehicle(120, 165000)
print(mitsubishi_spacestar)