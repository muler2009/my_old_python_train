            # String data types reminder

# Literals assignment
# first_name = "Muleta"
# last_name = "Taye"
# print(type(first_name))
# print(isinstance(first_name, str))

# constructore assignement
# food = str("pizza")
# print(type(food))
# print(isinstance(food, int))

# string concatination

# full_name = first_name + " " + last_name

# titlec = "Welcome to Python programming"
# print(titlec.center(25, "="))
# print("Cofee".ljust(16, ".") + "15ETB".rjust(6)) 
# print("Tea".ljust(17, ".") + "125ETB".rjust(6)) 



multiline = '''
Hey, how are you?                

I was just thinking if i reach you.   

            All good!

'''
print(multiline)

# string builting method
# print(f"title() method result : \n{multiline.title()}")
# print(f"title() method result : \n{multiline.replace('good', 'cool')}")
# print(f"Total number of character {len(multiline)}")
# print(f"Total number of character after whitespace removed {len(multiline.strip())}")
# print(f"Total number of character left whitespace removed {len(multiline.lstrip())}")
# print(f"Total number of character right whitespace removed {len(multiline.rstrip())}")

            # Integer types of data
value =90
print(type(value))
print(r"It's is an Intger type") if isinstance(value, int) else print(r"It's another type")

complex_value = 3+4j
print(type(complex_value))
print(f"Real value is : {int(complex_value.real)}")
print(f"Imaginary value is : {int(complex_value.imag)}")


gpa = float(3.33)
# print(abs(gpa))
# print(round(gpa))
# print(round(gpa,1))


import math

print(math.sqrt(gpa))
print(math.ceil(gpa))
print(math.floor(gpa))


