#Can cubes pile Vertically?  Bottom cube must be larger than top cube large
def pile_up_cubes(cubes):
    
    can_pile = "Yes"

    for index in range(len(cubes) - 1):
        if cubes[index] < cubes[index + 1]:
            can_pile = 'No'

    return can_pile
        