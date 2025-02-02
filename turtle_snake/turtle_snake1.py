''' turtle_snake1.py   贪吃蛇1  网上下载原程序  作者: Mahesh Sawant
用python内置turtle模块编写的简单游戏程序.
未修改(仅改变了移动速度值),仅用中文简要注释,供参考、学习、对照和存档.
蛇身动画移动算法:
游戏主循环每次循环从末尾开始遍历列表,让后个元素坐标移到前个元素坐标值.
列表第一个元素移动到蛇头head坐标.
游戏方法:
 1.蛇头正向左或向右移动时,按键盘向上(Up)键蛇头向上移动,按向下键(Down)蛇头向下移动.
 2.蛇头正向上或向下移动时,按键盘向左(Left)键蛇头向左移动,按向右键(Right)蛇头向右移动.
 3.操作移动蛇头去碰撞食物,即吃掉食物,记分增加10分.
 4.蛇头移动时不能碰到游戏屏幕边框,如碰撞则游戏失败.
 5.退出游戏只能关闭游戏屏幕窗口
认真对照turtle_snake2.py,turtle_snake3.py这2个逐步改写和turtle_snake.py扩展版本,
可学习掌握用类来创建对象(实例化)、面向对象和事件驱动等编程技术.
'''
import turtle # 导入turtle模块，调用其对象和函数等功能
import time # 导入python自带的时间模块库time,调用库time的函数或对象前加(time.)
import random # 导入random模块,调用其对象、类和函数等前加random.

delay = 0.1 #延迟时间变量设置

# Score记分变量初始化
score=0
high_score=0

# set up the screen 设置游戏窗口
wn=turtle.Screen() #创建窗口实例wn对象
wn.title("Snake Game by Mahesh Sawant")
wn.bgcolor("green") #设置游戏窗口背景颜色
wn.setup(width=600, height=600) #设置游戏窗口大小
wn.tracer(0) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(False)等效

# Snake head 设置蛇头
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop" #head.这样设变量将在其它函数中调用,而不必设定为全局变量

# Snake food 设置食物
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[] #初始化蛇身列表

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions 键盘(按上、下、左、右键)绑定的4个函数(),修改head.direction变量值
def go_up():
    if head.direction != "down": #如此时蛇头正向下移动时,将不会有反应
        head.direction="up"

def go_down():
    if head.direction != "up": #如此时蛇头正向上移动时,将不会有反应
        head.direction="down"

def go_left():
    if head.direction != "right": #如此时蛇头正向右移动时,将不会有反应
        head.direction="left"

def go_right():
    if head.direction != "left": #如此时蛇头正向左移动时,将不会有反应
        head.direction="right"

#自定义函数move(),蛇头根据head.direction变量值进行对应的方向产生移动
def move():
    if head.direction == "up":
        y=head.ycor() #获取蛇头现y坐标
        head.sety(y+10) #设蛇头y坐标为原坐标值增加10,效果为向上移动10

    if head.direction == "down":
        y=head.ycor()
        head.sety(y-10) #设蛇头y坐标为原坐标值-10,效果为向下移动10

    if head.direction == "left":
        x=head.xcor() #获取蛇头现x坐标
        head.setx(x-10) #设蛇头x坐标为原坐标值-10,效果为向左移动10

    if head.direction == "right":
        x=head.xcor()
        head.setx(x+10) #设蛇头x坐标为原坐标值+10,效果为向右移动10

# keyboard bindings 键盘绑定
wn.listen() #设置焦点接受按键亊件,下边语句是事件驱动(event-driven)语句
wn.onkeypress(go_up,"Up") #按键盘Up键调用go_up()函数
wn.onkeypress(go_down,"Down") #按键盘Down键调用go_down函数
wn.onkeypress(go_left,"Left") #按键盘Left键调用go_left函数
wn.onkeypress(go_right,"Right") #按键盘Right键调用go_right函数

# Main game loop  游戏主循环
while True:
    wn.update() #每次循环执行一次TurtleScreen刷新

    # Check for a collision with the border 每次循环检查头部是否与边框碰撞
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop" #未触发按键驱动事件前,头部停止不移动

        # Hide the segments  遍历列表segments,隐藏身体部份显示
        for segment in segments:
            segment.goto(1000,1000)

        # Clear the segments list  清除列表全部元素
        segments.clear()

        # Reset the score
        score=0 #初始化记分变量

        # Reset the delay
        #delay = 0.1

        pen.clear() #清除文字
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Check for a collision with the food 每次循环检测是否吃到食物
    if head.distance(food)<20:
        # move the food to a random spot
        x=random.randint(-285,285) #从-285到285中随机生成x
        y=random.randint(-285,285) #从-285到285中随机生成y
        food.goto(x,y) #食物到随机坐标位,示意新产生食物

        # Add a segment 增加列表元素,体现吃了食物后身体增长
        new_segment=turtle.Turtle() #创建食物海龟对象
        #new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup() #抬笔,移动时不留线条
        segments.append(new_segment) #将此对象加入列表未尾

        # Shorten the delay
        delay -= 0.001 #减少延迟时间,表现效果为蛇移动增速

        # Increase the score
        score+=10 #记分
        #让变量high_score保留最高分
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center",font=("Courier", 24, "normal"))

    # Move the end segment first in reverse order 产生蛇体移动的动画效果
    # 每次游戏主循环,列表都要以fo循环从末尾开始遍历,让后个元素坐标移到前个元素坐标值
    for index in range(len(segments)-1,0,-1): #循环到0则停止,列表第一个元素未动
        x=segments[index-1].xcor() #前个元素x坐标值
        y=segments[index-1].ycor() #前个元素y坐标值
        segments[index].goto(x,y) #让元素坐标移到前个元素坐标值

    # Move segment 0 to where the head is
    #每次游戏主循环,列表元素跟着蛇头移动的效果
    if len(segments)>0: #当列表元素个数大于0时,len(n)返回对象n的元素个数函
        x=head.xcor() #蛇头x坐标值
        y=head.ycor() #蛇头y坐标值
        segments[0].goto(x,y) #列表第一个元素移动到蛇头坐标

    move() #调用自定义函数move(),蛇头根据head.direction值进行对应的方向产生移动

    time.sleep(delay) #每次循环调用time模块的sleep()函数,暂停delay秒调整程序执行速度

wn.mainloop() # ?