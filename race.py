import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Pick a color:'")

colors = ["green", "red", "blue", "yellow", "violet", "indigo"]

y_coor = [-100, -60, -20, 20, 60, 100]

all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_coor[i])
    all_turtles.append(new_turtle)

#if bet is true, then the race will start
if bet:
    is_race_on = True

#while the race is on the for loop inside will continue to run.
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner :<")
        random_dis = random.randint(0, 10)
        turtle.forward(random_dis)



screen.exitonclick()
