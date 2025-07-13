from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()
turtle.setheading(90)

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.back(10)

def turn_clockwise():
    turtle.right(5)

def turn_anticlockwise():
    turtle.left(5)
def reset():
    turtle.reset()
    turtle.setheading(90)


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_clockwise,"d")
screen.onkey(turn_anticlockwise,"a")
screen.onkey(reset,"c")







screen.exitonclick()