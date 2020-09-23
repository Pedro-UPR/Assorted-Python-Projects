import turtle
import math

# CONSTANTS #

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
PI = math.pi

# FUNCTIONS #

def print_heading():
    print('Polygon Maker')
    print('–––––––––––––')

def take_number_of_sides():
    while True:
        numOfSides = input('Number of sides for the polygon: ')
        if numOfSides == '0' or numOfSides == '1' or numOfSides == '2':
            print('Can\'t form valid polygons with less that 3 sides...')
        else:
            try:
                numOfSides = abs(int(numOfSides)) # the abs() manages negatives
                return numOfSides
            except:
                print("That's not a number!\n")

def centralize_horizontally():
    turtle.dot()
    turtle.penup()
    turtle.backward((WINDOW_WIDTH / numberOfSides) / 2)
    turtle.pendown()

def centralize_vertically():
    turtle.penup()
    turtle.right(90)
    sideLength = WINDOW_WIDTH / numberOfSides
    height = sideLength / (2 * math.tan(PI/numberOfSides))
    turtle.forward(height)
    turtle.left(90)
    turtle.pendown()

def draw_shape(numberOfSides):
    loopCounter = numberOfSides
    while loopCounter > 0:
        turtle.forward(WINDOW_WIDTH / numberOfSides)
        turtle.left(360/numberOfSides)
        loopCounter -= 1

def continue_prompt():
    continuePrompt = input('Do you wish to continue? Y/N\n')
    if continuePrompt.upper() == 'Y':
        return True
    elif continuePrompt.upper() == 'N':
        return False
    else:
        print('Not valid input! Please use Y or N')

# EXECUTION #

print_heading()
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

programIsRunning = True
while programIsRunning:
    turtle.hideturtle()
    numberOfSides = take_number_of_sides()
    centralize_horizontally()
    centralize_vertically()
    draw_shape(numberOfSides)
    programIsRunning = continue_prompt()
    turtle.clearscreen()

print('Thank you for using the Polygon Maker!')

'''
Notes:
-program allows somewhat accurate vertical centralization (needs work)
'''
