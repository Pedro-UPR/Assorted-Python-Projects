import turtle
import random

# CONSTANTS #

FORCE_FACTOR = 7.5
WIDTH = 800
HEIGHT = 800
TARGET_WIDTH = int(WIDTH / 12)
TARGET_HEIGHT = int(HEIGHT / 12)
LEFT_BOUND = -1 * ((WIDTH / 2) - TARGET_WIDTH)
RIGHT_BOUND = (WIDTH / 2) - (2 * TARGET_WIDTH)
LOWER_BOUND = -1 * ((HEIGHT / 2) - TARGET_HEIGHT)
UPPER_BOUND = (HEIGHT / 2) - (2 * TARGET_HEIGHT)

# OBJECTS #
turtle = turtle.Turtle()
screen = turtle.screen()

# FUNCTIONS #

def set_window(width, height):
    screen.setup(width, height)

def square(horLen, vertLen):
    for count in range(4):
        if count % 2 == 0:
            turtle.forward(horLen)
            turtle.left(90)
        else:
            turtle.forward(vertLen)
            turtle.left(90)

def draw_target(x, y):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    square(TARGET_WIDTH, TARGET_HEIGHT)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.showturtle()

def aim_and_shoot():
    while True:
        angle = input('Angle: ')
        try:
            angle = float(angle)
            turtle.left(angle)
            break
        except:
            print('Invalid input!')
            continue
    while True:
        force = input('Force: ')
        try:
            distance = float(force) * FORCE_FACTOR
            turtle.forward(distance)
            break
        except:
            print('Invalid input!')
            continue

def player_wins(x, y):
    withinHorBound = x >= xCorTarget and x <= (xCorTarget + TARGET_WIDTH)
    withinVertBound = y >= yCorTarget and y <= (yCorTarget + TARGET_HEIGHT)
    if withinHorBound and withinVertBound:
        print('You Win!')
        print('Number of attempts:', numberOfAttempts)
        return True
    else:
        print('You Lose...')
        print('Number of attempts:', numberOfAttempts)
        return False

def try_again():
    while True:
        choice = input('Try again? (Y/N)\n')
        if choice.upper() == 'Y':
            turtle.goto(0, 0)
            turtle.setheading(0)
            return True
        elif choice.upper() == 'N':
            return False
        else:
            print('Invalid answer!')

def play_again():
    while True:
        choice = input('Play again? (Y/N)\n')
        if choice.upper() == 'Y':
            return True
        elif choice.upper() == 'N':
            return False
        else:
            print('Invalid answer!')

# EXECUTION #

program = True
set_window(WIDTH, HEIGHT)
while program is True:
    turtle.speed(0) # draws the game instantly
    xCorTarget = random.randint(LEFT_BOUND, RIGHT_BOUND)
    yCorTarget = random.randint(LOWER_BOUND, UPPER_BOUND)
    draw_target(xCorTarget, yCorTarget)
    currentGame = True
    numberOfAttempts = 1
    turtle.speed(3) # lets the player see motion
    while currentGame is True:
        aim_and_shoot()
        if player_wins(turtle.xcor(), turtle.ycor()):
            break
        numberOfAttempts += 1
        currentGame = try_again()
    program = play_again()
    screen.clearscreen()
