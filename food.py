from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.color("green")
        self.penup()
        self.refresh()

    def refresh(self):
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(x=random.randint(-280, 280), y=random.randint(-280, 280))


