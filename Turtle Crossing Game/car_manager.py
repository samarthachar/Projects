import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    move_distance = STARTING_MOVE_DISTANCE
    def __init__(self):
        super().__init__()
        self.penup()
        self.ypos = random.randint(-250,250)
        self.goto(300,self.ypos)
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))

    def move(self):
        self.forward(CarManager.move_distance)
    @classmethod
    def next_level(cls):
        cls.move_distance += MOVE_INCREMENT
        print(cls.move_distance)

