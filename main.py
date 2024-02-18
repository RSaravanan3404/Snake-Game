from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snaky!")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 10:
        score_board.increase_score()
        food.refresh()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_snake()
        score_board.reset_score()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            snake.reset_snake()
            score_board.reset_score()

screen.exitonclick()
