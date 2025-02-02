'''turtle_go_home1.py 海龟回家1  是网上下载turtle_go_home0.py版本的中文注释
1. 本程序存在游戏期间不断创建车辆，列表(car_list)一直在程序运行期增扩,不断地消耗内存和
   计算机的运算能力,程序逻辑上也有些不好理解.
2. 仅为便于阅读与注释,在不改变原程序逻辑和遵照原命令语句执行要求前提下,略改动.
游戏方法:
1.不断地按下并释放键盘上的Up(向上)键,让游戏海龟从屏幕底部向上穿过,到达屏幕项部而不被车辆碰到，则过关.
2.如发生碰撞则游戏结束,出现Game Over时,在游戏窗口现鼠标同时按鼠标键终止程序运行.
'''
import turtle #导入turtle模块,调用其对象、类和函数等前加turtle.
import time #导入time模块,调用其对象、类和函数等前加time.
import random #导入random模块,调用其对象、类和函数等前加random.

#car_manager 车辆管理部份
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] #车辆颜色列表
STARTING_MOVE_DISTANCE = 5 #初始移动距离变量设置
MOVE_INCREMENT = 10 #移动增量变量设置
THE_BOTTOM = -240 #车辆随机投放y轴底部坐标值变量设置
THE_TOP = 240 #车辆随机投放y轴顶部部坐标值变量变量设置

#创建车辆海龟函数
def create():
    new_car = turtle.Turtle() #创建海龟车辆new_car对象实例
    new_car.shape("square") #设置海龟形状,可选:arrow,turtle,circle,square,triangle,classic改变形状
    new_car.shapesize(1, 2) #设置海龟的拉伸因子和轮廓宽度
    new_car.color(random.choice(COLORS)) #从列表COLORS中随机选出的颜色来设置海龟车辆颜色
    new_car.setheading(180) #设置海龟车辆朝向180度,向屏幕左边
    new_car.penup() #抬起海龟画笔
    new_car.car_position = random.randint(THE_BOTTOM, THE_TOP) #车辆随机投放y轴范围内随机选出y坐标值
    new_car.goto(270, new_car.car_position) #移动海龟到坐标x=270,y=变量new_car.car_position
    return new_car #本函数返回值,海龟车辆new_car对象实例

#创建车辆管理类
car_list = [] #初始化车辆对象列表 *
class CarManager:
    """
    原本是将car_manager打造为控制单车。后面升级为车队管理
    """

    def __init__(self):
        #self.car_list = [] #原有语句
        #self.car_list.append(create()) #原有语句
        car_list.append(create()) #新建海龟车辆new_car对象实例加入列表
        self.car_generate_time = 0.1 #初始化控制车间距计数变量
        self.speed = STARTING_MOVE_DISTANCE #初始移动距变量离设置

    def move(self): #车辆横向移动方法，实现车辆自左向右的移动
        self.car_generate_time += 0.1 #每调用一次move方法,车辆次数加1

        if self.car_generate_time > 0.6: #调用6次move方法后,再新加入一辆，实际是控制车辆间距
            self.car_generate() #调用car_generate()方法新增1车辆
        #for i, car in enumerate(car_list): #等效下条,新加用于测试验证原编码有逻辑处理错误 *
        for car in car_list: #用fo ..in迭代车辆列表,遍历整个列表,让列表中的所有车辆向前移动 *
            car.forward(self.speed) #对应车辆向前进距离self.speed，实现车辆自左向右的移动
        #print(f'i={i}') #新加用于测试验证原编码有逻辑处理错误 *

    def car_generate(self): #新增车辆
        new_car = create() #调用自建函数创建海龟车辆new_car对象实例
        #self.car_list.append(new_car) #原有语句
        car_list.append(new_car) #新建海龟车辆new_car对象实例加入列表 *
        self.car_generate_time = 0.1 #初始化控制车间距计数变量

    def accelerate(self): #增加车辆移动距离,显示增速,level提升时调用
        self.speed += MOVE_INCREMENT # MOVE_INCREMENT=移动增量


#player创建玩家海龟
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(turtle.Turtle):
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
FONT = ("Courier", 24, "normal")

class Scoreboard(turtle.Turtle):
    """
    显示玩家的关数目，并适当提示Game Over
    """

    def __init__(self): #初始化启动语句属性设置
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 0
        self.game_up()

    def game_up(self): #显示游戏开始,处理升关(级)
        self.level += 1
        self.clear()
        self.write(f"level: {self.level}", font=FONT)

    def failed(self): # 显示游戏失败,结束
        self.goto(0, 0)
        self.write("Game Over", font=FONT)

# main
turtle.setup(width=600, height=600)
turtle.tracer(0) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(False)等效
# 创建玩家小乌龟（继承turtle),实现玩家响应上键移动
player = Player()
car_manager = CarManager()
# 创建scoreboard类，显示等级
scoreboard = Scoreboard()

turtle.onkey(player.move, "Up")
turtle.listen()

game_is_on = True
while game_is_on:
    #创建车类，（继承turtle)，
    #实现车辆自左向右的移动,间隔一定时间生成车辆,位置随机（Y）
    car_manager.move() #此语句有一问题，在游戏期间在不断创建车辆，列表一直在增扩!

    #如果未碰撞，且玩家的y坐标超出预定值，则成功完成,重新设置玩家海龟位置，并将level提升
    if player.ycor() > 280:
        player.go_back()
        scoreboard.game_up()
        car_manager.accelerate()

    #检测玩家海龟与所有车辆是否碰撞
    for car in car_list: #用fo ..in迭代车辆列表,遍历整个列表,判定海龟与车辆是否碰撞发生
        if abs(player.xcor() - car.xcor()) < 28 and abs(player.ycor() - car.ycor()) < 18:
            scoreboard.failed()
            game_is_on = False #该值设置为False,退出循环,游戏终止

    turtle.update() #执行一次TurtleScreen刷新
    time.sleep(0.1) #调用time模块的sleep()函数,暂停0.1秒

turtle.exitonclick() #bye()绑定到鼠标按键(鼠标点击事件),终止程序运行