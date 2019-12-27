import turtle
#
# a= (turtle.forward(100))
# b= (turtle.right(90))
# c= (turtle.forward(100))
# d= (turtle.right(90))
# e= (turtle.forward(100))
# f= (turtle.right(90))
# g= (turtle.forward(100))
# h= (turtle.color("red"))
# i= (turtle.right(30))
# j= (turtle.forward(100))
# k= (turtle.right(30))
# l= (turtle.backward(100))

'''for stpes in range(4):
    turtle.forward(100)
    turtle.right(90)
    for reStep in range(4):
        turtle.forward(80)
        turtle.right(90)'''

# nosteps=10
# for stpes in range(nosteps):
#     turtle.forward(50)
#     turtle.right(360/nosteps)
#     for reStep in range(nosteps):
#         turtle.forward(20)
#         turtle.right(360/nosteps)
# turtle.exitonclick() # This will stop turtle screen to go-off after completing the code

# Little more complex
# for color in ['blue' , 'red' , 'pink' , 'green']:
#     turtle.color(color)
#     for stpes in range(1):
#         turtle.forward(100)
#         turtle.right(70)
#         for restep in range(2):
#             turtle.forward(70)
#             turtle.right(60)
#

t= turtle.Pen()
t.color("green")
t.begin_fill()
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.end_fill()

t.up()
t.right(100)
t.forward(90)
t.color("red")
t.begin_fill()
t.circle(40)
t.end_fill()


turtle.exitonclick()