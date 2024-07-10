from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move_forward(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            self.goto(STARTING_POSITION)
