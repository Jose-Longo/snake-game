from turtle import Screen
import time
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

amount_of_food = random.randint(3, 5)
food_in_scene = []

snake = Snake(3)
for _ in range(amount_of_food):
    new_food = Food()
    food_in_scene.append(new_food)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    #Detect collision with food
    for food in food_in_scene:
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.update_score(increase=1)

    #Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    #Remove Food Randomly
    if random.randint(0, 1000) < 30:
        random_index = random.randint(0, len(food_in_scene)-1)
        for index in range(0, len(food_in_scene)-1):
            if index == random_index:
                food_in_scene[index].__del__()
                food_in_scene.remove(food_in_scene[index])

    #Create Food Randomly
    if random.randint(0, 1000) < 15:
        new_food = Food()
        food_in_scene.append(new_food)










screen.exitonclick()