# In Python, a list is a built-in data type used to store an ordered collection of items. 
# Lists are mutable, which means you can modify their elements by adding or removing items. 

users = ['Yonas', 'martinez', 'Hojuland', 'David', 45, 45.09, True]
movies = ["Jason Bourne", "Bricklayer", 'Body of lies', 'Delta force']
print(type(users))
print(f"Total items in the list is: {len(users)}")

print(f"Value is = {users[0]}")
# for val in users:
#     print(f"value at index {users.index(val)} is {val}")

# users += ['Johnatan']
users.insert(0, 'Movies')
users.extend(["BlackList", 'NoteBook']) 
print(users)

users.remove('Yonas')
print(users)

del users[0]
print(users)

movies.sort()
print(f"Sorted users list : {movies}")

numbers = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ]
list_comprehention = [val * 2 for val in numbers]
result=[]
for val in numbers:
    if val % 2 == 0:
        val**= 2

    result.append(val)
print(result)
print(sorted(result ,reverse=True))
print(f"Result from List Comphrehnsion: {list_comprehention}")

