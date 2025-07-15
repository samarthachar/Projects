from turtle import Turtle
STARTING_POSITIONS = [(0,0),(0,-20),(0,-40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self,position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        self.add_segment(self.squares[-1].position())
        #Add segment to self
    def move(self):
        for sq_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[sq_num - 1].xcor()
            new_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)