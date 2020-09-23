# This program takes in the time and transforms it into a clock
# This is the second version of this program.
# Improvements include:
# -divided program into functions for readability
# -user can now choose to repeat the program

import turtle
turtle = turtle.Turtle()
screen = turtle.screen()

screen.setup(500,500)

# FUNCTIONS #

def set_initial_conditions():
    turtle.hideturtle()
    turtle.left(90) # sets the starting angle to 90º
    turtle.speed(0) # makes the image draw without delay

def draw_clock():
    turtle.dot() # draws center dot
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(100,0)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()

def take_time():
    done = True
    while done:
        inputTime = input('Enter the time in hours: ')
        try:
            timeFlt = float(inputTime)
            return(timeFlt)
        except:
            print('Not a valid input! Please enter a number.')

def draw_hands(time):
    # draws the hour hand
    hours = int(time)
    hourHandAngle = hours*30
    turtle.pensize(2)
    turtle.right(hourHandAngle)
    turtle.forward(65)
    # sets turtle to origin
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.left(hourHandAngle)
    # draws the minute hand
    minutes = int(time*60)
    minuteHandAngle = minutes*6
    turtle.pensize(1)
    turtle.right(minuteHandAngle)
    turtle.forward(90)

def continue_prompt():
    while True:
        cont = input('Do you with to continue? Y/N\n')
        if cont.upper() == 'Y':
            screen.clearscreen()
            return True
        elif cont.upper() == 'N':
            return False
        else:
            print('Not a valid input! Please enter Y or N.')

# PROGRAM #

programIsRunning = True
while programIsRunning:
    set_initial_conditions()
    draw_clock()
    draw_hands(take_time())
    programIsRunning = continue_prompt()

print('Thank you for using this program!')

# NOTES #
# the program is quite a bit longer now, but it has added functionality and it's easier to modify
# the the redundant part where the input is turned to float and then int again
