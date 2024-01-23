import math
import random as rdm
from rps2 import play_rps

print(math.pi)
print(rdm.choice("1234"))


container = dir(rdm) # display everyting inside if modules
# for item in container:
#     print(item)
    
# it will display the currently running module nmae
print(__name__) 
def name_test():
    if math.__name__ == "random":
        return f"You are Runnning the {rdm.__name__} module"
    else:
        return f"Another module"
    
print(name_test())

play_rps()
    