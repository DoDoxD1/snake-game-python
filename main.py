from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
scoreboard.refresh_score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while snake.game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15:
        food.create_food()
        scoreboard.refresh_score()


screen.exitonclick()
