from turtle import  Turtle
import random

COLORS=["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10

class CarManager:

    def __init__(self):

        self.all_cars=[]
        self.car_speed= STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance==1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=5,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y= random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    #after player crosses finish line level is up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    def move_cars(self):
        for car_item in self.all_cars:
            car_item.backward(self.car_speed)