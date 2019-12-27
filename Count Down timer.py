import time
def countdown(num):
    print("Cont down is getting started")
    while num >= 0:
        yield num
        num = num-1
user_input = countdown(int(input("Please set an number to start Count Down: ")))
for x in user_input:
    print(x)
    time.sleep(3)


