# This is in Python In build function used to evaluate an argument in a single python code.
# eval() function is always going to convert the provided data into internal data type internally.
# eval function is most commonly used with keyboard input function
# Example

a=(eval("10+10"))
print(a)
print(type(a))
#----------------------
20
<class 'int'>

# So you do not need to specify which data type you are giving as input. similar way it can evaluate all other data type like String, Float, Boolean, List, etc..

b=eval(input("enter some argument"))
print(b)
#------------------------------
enter some argument20+30-10*3
20


