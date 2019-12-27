'''i = 0
numbers = []

while i < 6:
 print ("At the top i is %d" % i)
 numbers.append(i)
 i = i + 1
print ("Numbers now: ", numbers)
print ("At the bottom i is %d" % i)
print ("The numbers: ")
for num in numbers:
 print (num)

def counting (input):
    number=[]
    while input <10:
        print ("the number is %d" %input)
        number.append(input)
        input=input+1
    else:
        print("your number is out of range")

num=20
n=counting(num)
print (n)'''

counter='0'
while counter != '4':
    counter= input("Guess the correct number: ")
print("Congrats this is the right no")



