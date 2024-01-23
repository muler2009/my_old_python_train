def addition(num1, num2): # num1 and num2 are parameters placeholder 
    sum = num1 + num2
    print(f"Sum = {sum}")
    
addition(1,4) # arguments : the actual data when the function is called(mutable)

def returnTest(num1=1, num2=2): # num1 and num2 are parameters placeholder 
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

print(f"The sum  is {returnTest(1)}")

def multiple_items(*args):
    print(args)
    print(type(args))
    
multiple_items(1, 2, 6)
    
def multi_named_items(*args, **kwargs):
    return kwargs
    
    
print(multi_named_items(first=1, second="Man Utd"))

