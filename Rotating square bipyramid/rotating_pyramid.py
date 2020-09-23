import turtle

# creating screen
screen = turtle.Screen()
WIDTH = 500
HEIGHT = 500
screen.setup(WIDTH, HEIGHT)

# creating the turtles
line1 = turtle.Turtle()
line2 = turtle.Turtle()
mid_vector = turtle.Turtle()
top_side = turtle.Turtle()
bottom_side = turtle.Turtle()
grid = turtle.Turtle()

def setup():
    screen.bgcolor('black')

    line1.color('green')
    line1.speed(0)
    line1.hideturtle()
    line1.pensize(4)

    line2.color('green')
    line2.speed(0)
    line2.hideturtle()

    mid_vector.color('green')
    mid_vector.speed(0)
    mid_vector.hideturtle()
    mid_vector.pensize(3)

    top_side.color('green')
    top_side.speed(0)
    top_side.hideturtle()
    top_side.pensize(3)

    bottom_side.color('green')
    bottom_side.speed(0)
    bottom_side.hideturtle()
    bottom_side.pensize(3)

    grid.pensize(1)
    grid.speed(0)
    grid.hideturtle()

# goes to a point x,y without drawing in between
def go_to(turt, x, y):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()

# draws horizontal line
def mid_line(turt, left, right):
    go_to(turt, left[0], left[1])
    turt.goto(right)

# draws the side
def draw_sides(turt, vertex, left, right):
    go_to(turt, left[0], left[1])
    turt.goto(vertex)
    turt.goto(right)

# "animation"
def draw_angles(turt, top, bottom, right, left, x, y):
    go_to(turt, top[0], top[1])
    turt.goto(x, y)
    turt.goto(bottom)
    go_to(turt, right[0], right[1])
    turt.goto(x, y)
    turt.goto(left)
    go_to(turt, 0, 0)


# main function
def main():
    left_endpoint = (-90, 0)
    right_endpoint = (90, 0)
    top_endpoint = (0, 150)
    bottom_endpoint = (0, -100)

    setup()
    draw_sides(top_side, top_endpoint, left_endpoint, right_endpoint)
    draw_sides(bottom_side, bottom_endpoint, left_endpoint, right_endpoint)
    x1 = right_endpoint[0]
    x2 = left_endpoint[0]
    y1 = 0
    y2 = 0

    while True:
        if x1 > 0 and x1 % 2 == 0:
            y1 -= 5
        elif x1 < 0 and x1 % 2 == 0:
            y1 += 5

        if x2 < 0 and x2 % 2 == 0:
            y2 += 5
        elif x2 > 0 and x2 % 2 == 0:
            y2 -= 5

        draw_angles(line1, top_endpoint, bottom_endpoint, right_endpoint, left_endpoint, x1, y1)
        draw_angles(line2, top_endpoint, bottom_endpoint, right_endpoint, left_endpoint, x2, y2)
        line1.clear()
        line2.clear()

        if x1 <= left_endpoint[0]:
            x1 = right_endpoint[0]
        else:
            x1 -= 10
        if x2 >= right_endpoint[0]:
            x2 = left_endpoint[0]
        else:
            x2 += 10


        

main()
screen.mainloop()