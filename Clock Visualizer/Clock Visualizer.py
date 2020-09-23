import turtle

def setup():
    turtle.setup(500,600) #sets up the window size
    turtle.hideturtle()
    turtle.left(90)
    turtle.speed(0)


def draw_clock():
    turtle.dot()
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(100,0)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()

#variables
time = float(input('Enter the hour: ')) #gets the hour from the user

hours = int(time)
minutes = int(time*60)

hourHandAngle = hours*30 #the angle that corresponds to the hour hand
minuteHandAngle = minutes*6 #the angle that corresponds to the minute hand

#hour hand
turtle.pensize(2)
turtle.right(hourHandAngle) #sets the hour hand angle
turtle.forward(65) #draws hour hand

turtle.penup()
turtle.goto(0,0) #reset turtle to origin
turtle.pendown()
turtle.left(hourHandAngle) #resets the turtle to 12 o'clock

#minute hand
turtle.pensize(1)
turtle.right(minuteHandAngle) #sets the minute hand angle
turtle.forward(90) #draws minute hand
