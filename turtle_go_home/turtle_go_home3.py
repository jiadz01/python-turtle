'''turtle_go_home3.py  海龟回家3   对turtle_go_home2.py改写版
本版对车辆海龟类Car()作了修改,创建车辆时对形状、颜色、初始速度和升级后增速等,都利用随机函数从设置的列表中
随机选取,使画面更生动有趣.调整了游戏窗口颜色和游戏主循环中程序执行暂停0.03秒(30毫秒),动画更平顺自然.
主要技术要点:
1. 自定义一个继承Turtle的车辆子类Car,按一定数量和间隔创建长方形外形海龟车辆对象,并存放在car_list列表中.
   在该类的movo()方法实现车辆自右向左的移动,并到左边界时重新回到右边起点.
2. 车辆对象间隔由变量car_generate_time控制,它是拟创建车辆对象的x倍数(本例取9),
   在游戏主循环创建车辆对象时,只有拟创建对象数大于零,同时控制对象间隔的变量能被x整除时(%,取模,除法余数=0),
   才创建车辆对象,从而产生车辆对象间隔(本例取9,每间隔8次生成一辆).
3. 游戏主循环中每次循环用fo ..in迭代车辆car_list列表,遍历整个列表,让列表中的所有车辆调用类方法movo(),
   实现车辆自左向右不断移动的动画图象.
游戏方法:
1.不断地按下并释放键盘上的Up(向上)键,让游戏海龟从屏幕底部向上穿过,到达屏幕项部而不被车辆碰到，则过关.
2.如发生碰撞则游戏结束,出现Game Over时,按键盘Q键终止程序运行.
其又进一步改写和扩展版本详见:turtle_go_home4.py,turtle_go_home5.py.....
'''
import turtle #导入turtle模块,调用其对象、类和函数等前加turtle.
import time #导入time模块,调用其对象、类和函数等前加time.
import random #导入random模块,调用其对象、类和函数等前加random.

#常量设置和初始化部份
#车辆Car部份
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"] #车辆颜色列表,创建时随机选择其中之一
CAR_SHAPES = ["square","circle"] #车辆形状列表,创建时随机选择其中之一
STARTING_MOVE_DISTANCE = [1,1.3,2]#初始移动距离列表,创建时随机选择其中之一
MOVE_INCREMENT = [0.2,0.6,0.8 ]#游戏海龟每升一级,车辆移动增量列表设置,随机选择其中之一
THE_BOTTOM = -240 #车辆随机投放y轴底部坐标值变量设置
THE_TOP = 240 #车辆随机投放y轴顶部部坐标值变量变量设置
car_number = 10 #设置创建海龟车辆数
car_add = 5 #设置每提高一关添加辆车数
#游戏海龟player部份
STARTING_POSITION = (0, -280) #游戏海龟初始坐标
P_MOVE = 10 #设置当键盘Up键按下并释放时海龟移动距离

car_list = [] #初始化车辆对象列表
writer = turtle.Turtle() #创建书写海龟笔writer对象实例,下边调用相关函数时均要加前(writer.)指明从属关系
player = turtle.Turtle() #创建游戏海龟player对象实例,下边调用相关函数时均要加前(player.)指明从属关系

#自定义车辆海龟类Car()
class Car(turtle.Turtle):
    def __init__(self):
        super().__init__() #让父类Turtle的属性与子类Car关联
        self.shape(random.choice(CAR_SHAPES)) #设置海龟形状,创建时随机选择其中之一
        self.shapesize(1, 2) #设置海龟的拉伸因子和轮廓宽度
        self.color(random.choice(CAR_COLORS)) #从列表COLORS中随机选出的颜色来设置海龟车辆颜色
        self.setheading(180) #设置海龟车辆朝向180度,向屏幕左边
        self.penup() #抬起海龟画笔
        car_y = random.randint(THE_BOTTOM, THE_TOP) #车辆随机投放启始y轴范围内随机选出y坐标值
        self.goto(270, car_y) #移动海龟到启始坐标x=270,y=变量car_y
        self.speed = random.choice(STARTING_MOVE_DISTANCE) #初始移动距变量离设置,随机选择其中之一

    def move(self):
        self.forward(self.speed) #对应车辆向前进距离self.speed，实现车辆自右向左的移动
        if self.xcor() < -300: #如果车辆移动到左边界,即x坐标<-300
            self.hideturtle()
            self.setx(270) #重新设置x坐标=270,到右边边界起点,y坐标不变
            self.showturtle()

    def accelerate(self): #增加车辆移动距离,移动增速,level提升时调用
        self.speed += random.choice(MOVE_INCREMENT) # 在原有移动值基础上加一增量

#自定义初始化游戏文字提示海龟函数
def writer_create():
    writer.penup()
    writer.hideturtle()
    writer.goto(-250, 250) #书写海龟笔拟写游戏第几关文字说明的中心坐标位置

#自定义显示游戏第几关(级)函数
def writer_up():
    global level #设置level为全局变量
    FONT = ("Courier", 24, "normal")
    writer.clear() #书写海龟笔的所写文字清屏
    writer.write(f"level: {level}", font=FONT)
    level += 1

#自定义文字提示游戏失败,结束函数
def writer_failed():
    writer.goto(0, 0) #书写海龟笔写下边语句文字说明的中心坐标位置
    FONT = ("Courier", 24, "normal")
    writer.write("Game Over", font=FONT)

#自定义初始化游戏海龟函数
def player_create():
    player.shape("turtle") #设置海龟形状,可选:arrow,turtle,circle,square,triangle,classic改变形状
    player.setheading(90) #设置海龟朝向90度,向屏幕上边
    player.penup() #抬起海龟画笔,不留移动痕迹
    player.goto(STARTING_POSITION) #游戏海龟到初始坐标

#自定义游戏海龟前进移动函数
def player_move():
    player.forward(P_MOVE) #游戏海龟前进变量STARTING_POSITION的值

#游戏运行程序部份 main
turtle.setup(width=600, height=600) #设置游戏窗口大小
turtle.bgcolor('#6FBC99') #设置游戏窗口背景颜色,颜色十六进制码的选择详见color_rgb.py
turtle.tracer(0) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(False)等效
player_create() #游戏海龟初始化
writer_create() #文字提示海龟笔初始化
level = 1
writer_up() #显示游戏第1关(级)

turtle.listen() #设置焦点接受按键亊件,下边这条语句是事件驱动(event-driven)语句
turtle.onkey(player_move, "Up") #当键盘Up键按下并释放时,调用自定义函数player_move(),游戏海龟前进

car_generate_time = car_number * 9 #初始化控制车间距计数变量
game_is_on = True
 #游戏主循环,只有当game_is_on=False才会退出循环,游戏终止
while game_is_on:
    #创建车辆语句块
    if car_number > 0 and car_generate_time % 9 == 0:
        new_car = Car() #调用自建海龟车辆类Car()创建new_car对象实例
        car_list.append(new_car) #新建海龟车辆new_car对象实例加入列表car_list
        car_number -= 1
    if car_generate_time > 0: #当car_generate_time > 0时,每循环一次减1
        car_generate_time -= 1

    #车辆移动
    for car in car_list: #每次循环用fo ..in迭代车辆列表,遍历整个列表,让列表中的所有车辆向前移动
        car.move() #对应车辆向前进距离self.speed，实现车辆自左向右的移动,到左边界时回到起点重新开始

    #如果未碰撞，且玩家的y坐标超出预定值，则成功完成,重新设置玩家海龟位置，并将level提升
    if player.ycor() > 280:
        writer_up() #调用自定义函数,显示游戏第几关(级)
        player_create() #调用自定义函数,初始化游戏海龟
        for car in car_list: #用fo ..in迭代车辆列表,遍历整个列表,让列表中的所有车辆执行加速
            car.accelerate() #调用Car类中方法accelerate()提高本车速度
        car_number = car_add #每提高一关添加辆车
        car_generate_time = car_number * 9 #重新初始化控制车间距计数变量

    #每次循环检测玩家海龟与所有车辆是否碰撞
    for car in car_list: #用fo ..in迭代车辆列表,遍历整个列表,判定海龟与车辆是否碰撞发生
        if car.distance(player)<28: #turtle模块函数distance(),返回海龟对象car与player之间距离
            car.shapesize(1.8, 2.8) #设置海龟的拉伸因子和轮廓宽度增大,改变碰撞车辆外形变大而显眼
            writer_failed() #调用自定义文字提示游戏失败,结束函数
            game_is_on = False #该值设置为False,退出游戏主循环,游戏终止

    turtle.update() #每次循环执行一次TurtleScreen刷新
    time.sleep(0.03) #每次循环调用time模块的sleep()函数,暂停0.03秒(30毫秒),调整程序执行速度

turtle.onkeypress(turtle.bye,"q") #按键盘q键调用Screen()的专有方法bye(),退出程序运行
turtle.onkeypress(turtle.bye,"Q") #按键盘Q键调用Screen()的专有方法bye(),退出程序运行
turtle.mainloop()  #调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句