from turtle import *


#squere
speed(30)
width(7)
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()


#door
forward(40)
begin_fill()
color("yellow")
left(90)
forward(130)
right(90)
forward(60)
right(90)
forward(130)
end_fill()


#roof

penup()
goto(200,200)
pendown()
color("blue")
begin_fill()
right(140)
forward(150)
left(-262)
forward(150)
end_fill()



#window
color("cyan")
begin_fill()
penup()
goto(120,50)
pendown()
left(132)
forward(60)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(80)
end_fill()


#window 2
color("black")

penup()
goto(120,50)
pendown()
left(90)
forward(60)
left(90)
forward(80)
left(90)
forward(60)
left(90)
forward(80)


#patern

width(2)
color("black")
left(90)
forward(30)
left(90)
forward(80)
left(90)
forward(30)
left(90)
forward(40)
left(90)
forward(60)


#squere 2
penup()
goto(0,0)
pendown()


speed(30)
width(7)
color("black")

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)





#roof 2
penup()
goto(200,200)
pendown()
color("black")

right(-130)
forward(150)
left(-262)
forward(150)



















exitonclick()