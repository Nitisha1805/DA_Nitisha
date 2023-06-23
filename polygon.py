from turtle import *
speed('fastest')

distance = 100
sides = 6
for i in range(sides):
    pencolor('red')
    fd(distance)
    rt(360/sides)
    for i in range(sides):
        pencolor('green')
        fd(distance/2)
        rt(360/sides)
        write(i)

hideturtle()
mainloop() # This line is needed to keep the window open

