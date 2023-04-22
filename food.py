from turtle import Turtle
from random import randint


class Food:
    def __init__(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.penup()
        self.food.shapesize(stretch_len=.5,stretch_wid=.5)
        self.food.color("red")
        self.food.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.food.goto(x, y)
