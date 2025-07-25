from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
BEGINNING = -250
END = 250


class CarManager():
    def __init__(self):
        self.allcars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.seth(180)
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.goto(320, random.randint(BEGINNING,END))
            self.allcars.append(new_car)

    def move(self):
        for car in self.allcars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed = self.car_speed + MOVE_INCREMENT