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

if bet:
    is_race_on = True

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






#ETCH-A-SKETCH
# def move_forward():
#     tim.fd(10)
#
# def move_backward():
#     tim.backward(10)
#
# def clockwise():
#     t = tim.heading() + 10
#     tim.setheading(t)
#
# def counter_clockwise():
#     t = tim.heading() - 10
#     tim.setheading(t)
#
# def clear():
#     tim.reset()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=clockwise)
# screen.onkey(key="d", fun=counter_clockwise)
# screen.onkey(key="c", fun=clear)
screen.exitonclick()
