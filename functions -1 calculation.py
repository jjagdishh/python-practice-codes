total=100

def sum (a,b):
    total=a+b
    return total

def multiply (a,b):
    total=a*b
    return total

def division (a,b):
    total=a/b
    return total

def substract (a,b):
    total=a-b
    return total

n=sum(a=3,b=2)
print (n)

n=sum(b=3,a=2)    # this is called name argument if you want pass b first than a second
print (n)

n=multiply(20,2)
print (n)

n=division(20,2.9)
print (round(n))

n=substract(100,50)
print (n)

print (total)

#Note: "total" inside a finction is a "local variable". whereas "total" outside from a function is "global variable"

# what if user did not give an argument to the function like below example:

def multiply (a,b):
    total=a*b
    return total
    
n= multiply(5,) 
print(n)  # here program will give the error "missing 1 required positional argument: 'b'" 

# but you can give a default argument to the function like:

def multiply (a,b=0):
    total=a*b
    return total
    
n= multiply(5,)
print(n) 

# Note if user now give any argument for "b" default argument in function will be ignored

def multiply(a, b=0):
    total = a * b
    return total


n = multiply(5,3 )
print(n)