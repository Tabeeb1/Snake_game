from turtle import Turtle

positions = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]


    def create_snake(self):
        for position in positions:
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.snakes.append(new_snake)


    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[snake-1].xcor()
            y = self.snakes[snake-1].ycor()
            self.snakes[snake].goto(x,y)
        self.head.forward(20)




        if self.snakes[0].xcor() == 360:
            self.snakes[0].goto(-280,y)
            self.snakes[1].goto(-290, y)
            self.snakes[1].goto(-300, y)

        if self.snakes[0].ycor() == 360:
            self.snakes[0].goto(x, -280)
            self.snakes[1].goto(x, -290)
            self.snakes[1].goto(x, -300)

        if self.snakes[0].xcor() == -360:
            self.snakes[0].goto(280,y)
            self.snakes[1].goto(290, y)
            self.snakes[1].goto(300, y)

        if self.snakes[0].ycor() == -360:
            self.snakes[0].goto(x, 280)
            self.snakes[1].goto(x, 290)
            self.snakes[1].goto(x, 300)





    def up(self):
        if self.head.heading() != 270:
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
