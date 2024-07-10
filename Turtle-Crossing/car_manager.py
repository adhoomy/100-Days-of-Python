from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
SPEED_INCREASE = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.speed(self.car_speed)
            car.goto(300, random.randint(-230, 230))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed += SPEED_INCREASE
