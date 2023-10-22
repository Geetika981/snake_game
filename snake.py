STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.create_segment(pos)

    def create_segment(self, pos):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(pos)
        self.segments.append(tim)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.create_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)