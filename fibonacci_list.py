'''Note: 
To generate fibonacci numbers 
	0,1,1,2,3,5,8,13,21----> the sum of first two number in series called fibonacci numbers 
	like third number is sum of first two numbers then next 4th number is the sum of previous number'''

def fibonacci(b):
    a=0
    b=b
    while True:
        yield a
        a,b = b,a+b

num1 = int(input(" Please input an number to genrate fibonacci list: "))
num = int(input("enter break point number"))
for n in fibonacci(num1):
    if n >= num:
        break
    print(n)
