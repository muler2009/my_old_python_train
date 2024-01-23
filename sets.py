# Sets are collection data types in python used to store ordered ans unique value
# No duplicate value is allowed 
number = {1, 2, 3, 4, 5, 6}
numbers = set((1, 2, 3, 4, 5, 6))

print(type(number))
print(type(numbers))
print(f"The lenght of set : {len(numbers)}")

numbers.add(8)
print(numbers) 

# True is a dupe of 1, False is dupe of 0
set2 = {1, True, 2, False, 3, 5, 6, 0}
print(set2)

print(2 in set2) # check if the value is in a set 

# it is impossible to refer to an element in the set with an index value like in other collection data types

# Methods
morenums = {9, 10, 12}
set2.update(morenums)
print(set2)

# set specific operation
set1 = {1, 2, 3, 5, 6}
set3 = {2, 5, 9, 3, 6, 4}
union = set1.union(set3)
intersection = set1.intersection(set3)
difference = set3.difference(set1)
print(f"Merged sets: {union}")
print(f"Intersection: {intersection}")
print(f"difference of set1 and set3: {difference}")


A = {1, 2, 3, 5, 6}
B = {2, 5, 9, 3, 6, 4}
A.intersection_update(B) # update set A with the intersection of the two set
print(f"intersection_update is:  {A}")

A.symmetric_difference_update(B) # update set A with the difference  of the two set
print(f"symmnetric updates {A}")
