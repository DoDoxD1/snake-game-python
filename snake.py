import time
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake_box(self, i):
        box = Turtle("square")
        box.color("white")
        box.speed("fastest")
        box.penup()
        box.setpos(0 - (i * 20), 0)
        self.snake_body.append(box)

    def create_snake(self):
        for i in range(0, 3):
            self.create_snake_box(i)

    def detect_walls_collision(self, scoreboard):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            scoreboard.refresh_score()
            self.reset()

    def detect_snake_collision(self, scoreboard):
        for box in self.snake_body[1:]:
            if self.head.distance(box) < 10:
                scoreboard.refresh_score()
                self.reset()

    def reset(self):
        for box in self.snake_body:
            box.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            prev_box = self.snake_body[i - 1]
            box = self.snake_body[i]
            box.goto(prev_box.xcor(), prev_box.ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            time.sleep(0.1)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            time.sleep(0.1)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            time.sleep(0.1)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            time.sleep(0.1)
