import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#to move the turtle up
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # detect when turtle has reached the top
    if player.ycor() > 270:
        print("reached end")
        player.goto(0, -280)

        #update scoreboard
        scoreboard.point()

        #increase car speed
        car_manager.level_up()

    #detect collision with a car
    for each_car in car_manager.allcars:
        if player.distance(each_car) < 25:
            game_is_on = False
            print("Game over")
            scoreboard.game_over()

screen.exitonclick()
