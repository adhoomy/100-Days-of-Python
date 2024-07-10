from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    car_manager.new_car()
    car_manager.move_cars()
    screen.update()

    if turtle.ycor() > 280:
        turtle.at_finish_line()
        car_manager.increase_speed()
        scoreboard.level_up()

    for car in car_manager.cars:
        if turtle.distance(car) < 20:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
