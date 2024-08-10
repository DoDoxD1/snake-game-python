from turtle import Turtle
from scoreboard import ScoreBoard
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.game_on = True
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for i in range(0, 3):
            box = Turtle("square")
            box.color("white")
            box.penup()
            box.setpos(0 - (i * 20), 0)
            self.snake_body.append(box)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            prev_box = self.snake_body[i - 1]
            box = self.snake_body[i]
            box.goto(prev_box.xcor(), prev_box.ycor())
        self.head.forward(MOVE_DISTANCE)
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            self.game_on = False
            ScoreBoard().game_over()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
