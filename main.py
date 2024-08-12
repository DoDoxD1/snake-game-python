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
screen.onkey(scoreboard.stop_game, "c")

while scoreboard.game_on:

    # update screen
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.create_food()
        snake.create_snake_box(len(snake.snake_body) - 1)
        scoreboard.gain_score()

    # detect wall collision
    snake.detect_walls_collision(scoreboard)

    # detect self collision
    snake.detect_snake_collision(scoreboard)

screen.exitonclick()
