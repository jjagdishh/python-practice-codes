'''apple = 10
banana = 20
mango = 30

if apple < 100:
    print ("there are less apple in the store")
else:
    print ("There are enough apples in the store ")

if banana > mango:
    print ("there are enough bananas in the store")
else:
    print ("mango's are less in the store")'''

print ("'This is a dark night' and You are walking through a Jungle! \nyou found a house there with two doors \nDoor 1= Black \nDoor 2= White")
print ("which door you are going to choose! 1 or 2 ?")
door = input("door number")

if door == "1":
    print ("you are now into a lion cave")
    print ("Now you have two options \nfirst-1 you can stay calm \nSecond-2 you should fight with lion")
    print ("Which option you will choose 1 or 2 ")
    option=input()
    if option == "1":
        print("Lion will eat you")
    elif option == "2":
        print ("you are a daring person and you can beat the lion")
    else:
        print("You have no other choice")
elif door == "2":
    print ("you reached to your home \n good job done")
else:
    print ("This is a bad option",door)




