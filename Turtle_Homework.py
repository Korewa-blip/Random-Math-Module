import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(500,400)
polygon=turtle.Turtle()
num_side=4
side_length=120
angle=360/(num_side)
for i in range(num_side):
 polygon.forward(side_length)
 polygon.right(angle)
turtle.done()