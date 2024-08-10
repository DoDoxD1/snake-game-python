from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while snake.game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()


screen.exitonclick()
