#class_person_calc_age

#create a person class. Include name, country and date of birth attributes. 
#Implement a method to determine the person's age.

def __init__(self, *, name: str, dob: str, country: str) -> None:
    self.name = name
    self.dob = dob
    self.country = country
        
    
    def get_age(self.dob):
        return self.dob[:4]

def main() -> None:
    person = Person()

print(person.get_age())



if __name == '__main__':
    main()
    
