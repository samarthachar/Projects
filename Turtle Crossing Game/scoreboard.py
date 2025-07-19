from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,270)
        self.level = 1
        self.write(f"Level: {self.level}", font=FONT)
    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)
    def end_game(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
