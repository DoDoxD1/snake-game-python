from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.game_on = True
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
        self.snake_body[0].forward(MOVE_DISTANCE)
        if self.snake_body[0].xcor() > 280:
            self.game_on = False

    def up(self):
        self.snake_body[0].setheading(90)

    def down(self):
        self.snake_body[0].setheading(270)

    def left(self):
        self.snake_body[0].setheading(180)

    def right(self):
        self.snake_body[0].setheading(0)
