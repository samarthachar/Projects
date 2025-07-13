from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(height=400, width=500)
is_race_on = False
all_turtles = []
colours = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]



y = -100

for turtle_index in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x =- 230, y = y)
    new_turtle.color(colours[turtle_index])
    y += 33.33333
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0,10))