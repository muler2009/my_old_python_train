#loops
# incrementer = 1
# while incrementer <= 10:
#     incrementer += 1
#     if incrementer % 2 != 0:
#         continue
#     print(incrementer)
   
   
# incrementer = 1
# while incrementer < 10:
#     incrementer +=1 
#     if incrementer == 5:
#        continue
#     print(incrementer)
# else: # is executed when the loop end if break used else wouldn't execute
#     print(f"Value is now equal to {incrementer}")
    
names = ['Dave', 'Sara', 'Joha']
actions = ["codes", "python", "fastAPI"]
# for val in names:
#     if val == 'Sara':
#         continue
#     print(val)
    
# for x in range(5, 100, 5):
#     print(x)
# else:
#     print(r"Glad that's over")

for name in names:
    for action in actions:
        print(f"{name} {action}.")