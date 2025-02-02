'''turtle_go_home5.py  海龟回家5   对turtle_go_home4.py的升级优化版
本版增加了游戏窗口高(680),使游戏文字提示显示更方便.增加一个画笔对象pen,画出游戏海龟起跑线和终点线.
增加游戏海龟颜色列表turtle_colors,创建游戏海龟时,从颜色列表的头到尾顺序,依次循选择海龟颜色.
游戏海龟依次循选择海龟颜色有二种方法实现:A.固定从列表头取出颜色元素值设置海龟充填色后,再将该元素添加到
该列表末尾,按此依次循环操作.缺点是语句较多并不断地在改变列表元素顺序.B.与游戏关数level结合,以关数除以
颜色列表中的元素个数,取模(求余数),按此值为列表索引值来进行海龟颜色设置,与程序配合最好.
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
2.如发生碰撞则游戏结束,出现Game Over时,按键盘Q键终止程序运行,按键盘空格键可重新开始游戏.
其又进一步改写和扩展版本详见:turtle_go_home.py
'''
import turtle #导入turtle模块,调用其对象、类和函数等前加turtle.
import time #导入time模块,调用其对象、类和函数等前加time.
import random #导入random模块,调用其对象、类和函数等前加random.

#常量设置和初始化部份
#车辆Car部份
CAR_COLORS = ["red", "orange", "yellow", "green", "blue",
              "purple", "pink"] #车辆颜色列表,创建时随机选择其中之一
CAR_SHAPES = ["square","circle"] #车辆形状列表,创建时随机选择其中之一
STARTING_MOVE_DISTANCE = [1,1.3,2]#初始移动距离列表,创建时随机选择其中之一
MOVE_INCREMENT = [0.2,0.6,0.8 ]#游戏海龟每升一级,车辆移动增量列表设置,随机选择其中之一
THE_BOTTOM = -200 #车辆随机投放y轴底部坐标值变量设置
THE_TOP = 280 #车辆随机投放y轴顶部部坐标值变量变量设置
car_number = 10 #设置创建海龟车辆数
car_add = 5 #设置每提高一关添加辆车数
#游戏海龟turtle部份
STARTING_POSITION = (0, -240) #游戏海龟初始坐标
P_MOVE = 10 #设置当键盘Up键按下并释放时海龟移动距离
turtle_colors = ["black", "orange", "yellow", "green", "blue",
              "purple", "red"] #游戏海龟颜色列表,创建时从头到尾依顺序排列选择
car_list = [] #初始化车辆对象列表
writer = turtle.Turtle() #创建书写海龟笔writer对象实例,下边调用相关函数时均要加前(writer.)指明从属关系
pen = turtle.Turtle() #创建绘图海龟笔pen对象实例,下边调用相关函数时均要加前(pen.)指明从属关系

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

    def car_ht(self):
        self.hideturtle() #隐藏海龟车辆

#自定义初始化游戏文字提示海龟函数
def writer_create():
    writer.penup()
    writer.hideturtle() #隐藏海龟画笔

#自定义显示游戏第几关(级)函数
def writer_up():
    global level #设置level为全局变量
    FONT = ("Courier", 18, "normal") #设置字体名字、字大小、字类型
    writer.pencolor("blue") # 设置海龟画笔颜色
    writer.clear() #书写海龟笔的所写文字清屏
    writer.goto(-276, 310) #书写海龟笔拟写游戏第几关文字说明的中心坐标位置
    level += 1
    writer.write(f"level: {level}", align="left", font=FONT)

#自定义文字提示游戏失败,结束函数
def writer_failed():
    writer.goto(-276, 280) #书写海龟笔写下边语句文字说明的中心坐标位置
    FONT = ("Courier", 18, "bold") #设置字体名字、字大小、字类型
    writer.pencolor("red") # 设置海龟画笔颜色
    writer.write("Crash! Game Over.",align="left", font=FONT)
    turtle.stamp() #加一个碰撞时海龟位置印章以便观察
    writer_reset(0,-290)

#自定义文字提示游戏重新开始,2个行参分别为字体中间下部位置坐标x,y
def writer_reset(x=0,y=-210):
    writer.pencolor("blue") # 设置海龟画笔颜色
    writer.goto(x,y)
    writer.write("Press space key to start play.",
          align="center", font=("Courier", 22, "bold")) #显示出操作提示文字
    writer.goto(x,y-30)
    writer.write("Press Q key to exit.",
              align="center", font=("Courier", 22, "bold"))

#自定义初始化游戏海龟函数
def turtle_create():
    global turtle_colors,level #设置turtle_colors为全局变量
    turtle.pencolor("black") #设置海龟(边沿的颜色)颜色为black
    ### A.第一种循环设海龟颜色语句块
    color = turtle_colors.pop(0) #弹出颜色列表turtle_colors中排第一的颜色元素赋予变量color
    turtle.fillcolor(color) #设置海龟充填颜色为变量color
    turtle_colors.append(color) #将变量color的颜色元素添加到列表turtle_colors末尾
    ### B.第二种循环设海龟颜色语句,与上边三条语句等效,这二种方法可在命令前用注释#选择其中之一运行
    #turtle.fillcolor(turtle_colors[(level % 7)]) #设置海龟充填颜色为列表第(level % 7)索引的元素值
    ###
    turtle.shape("turtle") #设置海龟形状,可选:arrow,turtle,circle,square,triangle,classic改变形状
    turtle.setheading(90) #设置海龟朝向90度,向屏幕上边
    turtle.penup() #抬起海龟画笔,不留移动痕迹
    turtle.goto(STARTING_POSITION) #游戏海龟到初始坐标

#自定义游戏海龟前进移动函数
def turtle_move():
    turtle.forward(P_MOVE) #游戏海龟前进变量STARTING_POSITION的值



#游戏主循环
def game():
    global car_number,writer,level
    writer_up() #显示游戏第1关(级)
    turtle.clearstamps() #删除海龟印章(如果有)
    turtle.onkey(None, "space") #关闭了按键盘空格键调用game()函数进行游戏
    turtle.onkey(turtle_move, "Up") #当键盘Up键按下并释放时,调用自定义函数turtle_move(),游戏海龟前进
    car_generate_time = car_number * 9 #初始化控制车间距计数变量
    game_is_on = True
     #游戏主循环,只有当game_is_on=False才会退出循环,游戏终止
    while game_is_on:
        #创建车辆语句块
        if car_number > 0 and car_generate_time % 9 == 0:
            new_car = Car() #调用自建海龟车辆类Car()创建new_car对象实例
            car_list.append(new_car) #新建海龟车辆new_car对象实例加入列表car_list
            car_number -= 1 #等效car_number = car_number - 1
        if car_generate_time > 0: #当car_generate_time > 0时,每循环一次减1
            car_generate_time -= 1

        #车辆移动
        for car in car_list: #每次循环用fo ..in迭代车辆列表,遍历整个列表,让列表中的所有车辆向前移动
            car.move() #对应车辆向前进距离self.speed，实现车辆自左向右的移动,到左边界时回到起点重新开始

        #如果未碰撞，且玩家的y坐标超出预定值，则成功完成,重新设置玩家海龟位置，并将level提升
        if turtle.ycor() > 310:
            turtle.stamp() #加一个成功完成时海龟位置印章以便观察
            turtle_create() #调用自定义函数,初始化游戏海龟
            writer_up() #调用自定义函数,显示游戏第几关(级)
            for car in car_list: #用fo ..in迭代车辆列表,遍历整个列表,让列表中的所有车辆执行加速
                car.accelerate() #调用Car类中方法accelerate()提高本车速度
            car_number = car_add #每提高一关添加辆车
            car_generate_time = car_number * 9 #重新初始化控制车间距计数变量

        #每次循环检测玩家海龟与所有车辆是否碰撞
        for car in car_list: #用fo ..in迭代车辆列表,遍历整个列表,判定海龟与车辆是否碰撞发生
            if turtle.distance(car)<28: #turtle模块函数distance(),返回海龟对象turtle与car之间距离
                car.shapesize(1.8, 2.8) #设置海龟的拉伸因子和轮廓宽度增大,改变碰撞车辆外形变大而显眼
                writer_failed() #调用自定义文字提示游戏失败,结束函数
                game_is_on = False #该值设置为False,退出游戏主循环,本次游戏终止

        turtle.update() #每次循环执行一次TurtleScreen刷新
        time.sleep(0.03) #每次循环调用time模块的sleep()函数,暂停0.03秒(30毫秒),调整程序执行速度
    turtle.onkey(None, "Up") #关闭了当键盘Up键按下并释放时,调用自定义函数turtle_move(),游戏海龟前进
    turtle.onkey(pre_game, "space") #按键盘空格键调用pre_game()函数进行重新启动游戏

#重新(失败后)启动游戏主循环前期处置
def pre_game():
    global car_number,number,level
    car_number = number #重新初始化创建海龟车辆数
    for car in car_list: #用fo ..in迭代车辆列表,遍历整个列表,让列表中原有的所有车辆隐藏
        car.car_ht() #调用自定义Car()类中的方法car_ht,实现车辆从屏幕显示中删除
    car_list.clear() #清空列表中所有元素
    level = 0
    turtle_create() #调用自定义函数,初始化游戏海龟
    game() #调用自定义游戏主循环

#游戏运行程序部份 main
def main():
    global level,car_number,car_list,number
    turtle.setup(width=600, height=680) #设置游戏窗口大小
    turtle.bgcolor('#6FBC99') #设置游戏窗口背景颜色,颜色十六进制码的选择详见color_rgb.py
    turtle.tracer(0) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(False)等效
    level = 0
    turtle_create() #游戏海龟初始化
    writer_create() #文字提示海龟笔初始化
    number = car_number #变量number保留车辆设置数,供(失败后)重新启动游戏主循环前期处置用
    writer_reset(0,-290) #调自定义writer_reset()函数,在指定x=0,y=-290坐标显操作或退出提示
    #用画笔pen画出起下部跑蓝色线和上部到家绿色终点饯
    pen.pensize(3)
    pen.pencolor("blue") # 设置海龟画笔pen颜色
    pen.up() #抬起画笔,不留移动痕迹
    pen.ht() #隐藏海龟,还可用hideturtle()
    pen.goto(-276,-250)
    pen.pd() #放下画笔准备画图, 还可用down(),pendown()
    pen.goto(276,-250)
    pen.up() #抬起画笔
    pen.pencolor("green") # 设置海龟画笔pen颜色
    pen.goto(-80,312)
    pen.pd() #放下画笔准备画图, 还可用down(),pendown()
    pen.goto(180,312)
    turtle.update() #执行一次TurtleScreen刷新,画出上述绘画图象

    turtle.listen() #设置焦点接受按键亊件,下边这条语句是事件驱动(event-driven)语句
    turtle.onkey(None, "Up") #关闭了当键盘Up键按下并释放时,调用自定义函数player_move(),游戏海龟前进
    turtle.onkey(game, "space") #按键盘空格键调用game()函数进行游戏
    turtle.onkeypress(turtle.bye,"q") #按键盘q键调用Screen()的专有方法bye(),退出程序运行
    turtle.onkeypress(turtle.bye,"Q") #按键盘Q键调用Screen()的专有方法bye(),退出程序运行
    return "turtle_go_home: main() END    EVENTLOOP"

#程序实际执行起点
if __name__ == "__main__":   # execute only if run as a script
    msg = main()    #从这里开始执行本程序命令,调用程序主函数main()
    print(msg) #在Python shell窗口或界面打印
    turtle.mainloop()  #调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句