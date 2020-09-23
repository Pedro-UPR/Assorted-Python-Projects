"""
The program has been updated and is now Polygon Maker v2
Oct 15, 2019
"""

import turtle

turtle.setup(600,600) #sets the screen to 600x600 pixels
program = True #this variable determines wether the program runs

print('Polygon Maker:')
print('––––––––––––––')

while program == True:
    turtle.hideturtle()

    #number of sides the polygon should have
    numberOfSides = input('How many sides should the polygon have? \n')

    try:
        numberOfSides = int(numberOfSides)
    except:
        print("That's not a number!\n") #catches potential error from entering letters

    if type(numberOfSides) == type(0):
        numberOfTimes = numberOfSides #number of times the loop should be run

        turtle.penup()
        turtle.backward((500/numberOfSides)/2) #centralizes the shape horizontally
        turtle.pendown()

        while numberOfTimes > 0:
            turtle.forward(500/numberOfSides) #draws a side
            turtle.left(360/numberOfSides) #makes an angle
            numberOfTimes -= 1 #counter determines the number of times

    continueLoop = 0 #this variable determines wether the program should continue

    while continueLoop == 0:
        continuePrompt = input('Continue? (Y/N)\n')

        if continuePrompt.upper() == 'Y': #clears screen and runs the program again
            turtle.clearscreen()
            continueLoop = 1
        elif continuePrompt.upper() == 'N': #stops running the program
            continueLoop = 1
            program = False
        else: print('That\'s not a valid answer!') #runs the continue prompt again

print('Thank you for using!')

# Notes:
    # program dies if you enter a character in the first prompt (Fixed with try-except)
    # not centralized vertically
    # try changing it to functions
