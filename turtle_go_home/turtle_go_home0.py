'''turtle_go_home0.py  海龟回家  网上下载
存在游戏期间不断创建车辆，列表(car_list)一直在增扩!
原程序分四个模块，均将其合并在此.
中文注释是原有的,程序逻辑上有些不好理解,存档对照
'''
#car_manager
from turtle import Turtle,Screen
import time
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
THE_BOTTOM = -240
THE_TOP = 240


def create():
    new_car = Turtle()
    new_car.shape("square")
    new_car.shapesize(1, 2)
    new_car.color(random.choice(COLORS))
    new_car.setheading(180)
    new_car.penup()
    new_car.car_position = random.randint(THE_BOTTOM, THE_TOP)
    new_car.goto(270, new_car.car_position)
    return new_car


class CarManager:
    """
    原本是将car_manager打造为控制单车。后面升级为车队管理
    """

    def __init__(self):
        self.car_list = []
        self.car_list.append(create())
        self.car_generate_time = 0.1
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.car_generate_time += 0.1

        if self.car_generate_time > 0.6:
            self.car_generate()
        for car in self.car_list:
            car.forward(self.speed)

    def car_generate(self):
        new_car = create()
        self.car_list.append(new_car)
        self.car_generate_time = 0.1

    def accelerate(self):
        self.speed += MOVE_INCREMENT



#player
#from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_back(self):
        self.goto(STARTING_POSITION)

#scoreboard
#from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    显示玩家的关数目，并适当提示Game Over
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 0
        self.game_up()

    def game_up(self):
        self.level += 1
        self.clear()
        self.write(f"level: {self.level}", font=FONT)

    def failed(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT)


# main
#import time
#from turtle import Screen
#from player import Player
#from car_manager import CarManager
#from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
# TODO: 1.创建玩家小乌龟（继承turtle),实现玩家响应上键移动
player = Player()
car_manager = CarManager()
# TODO: 2.1 创建scoreboard类，显示等级
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # TODO: 2.创建车类，（继承turtle)，实现自左向右的移动

    # # TODO: 3.随机使得车对象的位置随机生成（Y），生成时间要间隔一定时间，每次生成数量，放置玩家没法玩。
    car_manager.move()
    # TODO: 5.如果未碰撞，且玩家的X坐标超出预定值，重新设置玩家位置，并将level提升
    if player.ycor() > 280:
        player.go_back()
        scoreboard.game_up()
        car_manager.accelerate()
    # TODO: 4.检测玩家与车辆的碰撞信息（所有）？列表处理？

    for car in car_manager.car_list:
        if abs(player.xcor() - car.xcor()) < 28 and abs(player.ycor() - car.ycor()) < 18:
            scoreboard.failed()
            game_is_on = False

    screen.update()

screen.exitonclick()