f=input("enter the file name")
file=open(f,"w")

while True:
    d=input("Please input your string.. ")
    file.write(d)
    con=input("do you want to continue writing 'yes|no'")
    if con=="no":
        print("Thanks for your input")
        file.close()
        break