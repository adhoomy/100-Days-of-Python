from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=700, height=350)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y_cord = 125
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-300, y=y_cord)
    y_cord -= 50
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 330:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won the bet. The {winner} turtle is the winner.")
            else:
                print(f"You've lost the bet. The {winner} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
