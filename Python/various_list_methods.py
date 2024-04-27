#various_list_methods.py
animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']
animals += ['Raccoon'] + wild_animals
animals.pop(2)
animals.pop()
animals.insert(2, 'Moose')
print(animals)

'''
Easy
Problem Description
Create a program to perform operations on a list using various list methods.

Suppose we have two lists as follows:

animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']
Perform these operations on the animals list:

Add 'Raccoon' to the end of the animals list.
Add all the elements from wild_animals to the end of the animals list.
Remove the third element from the animals list using the pop() method.
Remove the last element from the animals list using the pop() method.
Insert 'Moose' at the third position in the animals list.
Print the animals list.
Example
Expected Output

['Dog', 'Cat', 'Moose', 'Tiger']



Version 1

animals = ['Dog', 'Cat']
wild_animals = ['Tiger', 'Coyote']

# perform list operations
animals = animals + ['Racoon'] + wild_animals
animals.pop(2)
animals.pop(-1)
animals.insert(2, 'Moose')
print(animals)


Version 3
animals = ['Dog', 'Cat'] + ['Raccoon'] + ['Tiger', 'Coyote']; del animals[2]; del animals[-1]; animals.insert(2, 'Moose'); print(animals)

'''