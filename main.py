import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    #collision detect
    for single_block_car in car_manager.all_cars:
      if single_block_car.distance(player) < 25:
          game_is_on=False

    #detect successfull crossing ans restart and increase speed
      if player.is_at_finishline():
         player.go_to_start()
         player.speed()
         car_manager.level_up()
         scoreboard.increase_levelup()


screen.exitonclick()


