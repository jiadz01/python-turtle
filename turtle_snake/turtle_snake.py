'''turtle_snake.py   贪吃蛇   turtle_snake3.py的优化完善扩展版本  2022.1.18
新增对食物海龟进行形状和颜色,依次从列表中选择元素设置.
新增游戏蛇头碰撞身体的判定语句,如碰撞则游戏失败.
由于每台运行本程序的计算机运行速度不同,可对常量DELAY值设置进行调整改变,让动画更自然和流畅.
主要技术要点:
 1.自定义蛇身各段海龟Segment类,蛇每吃到食物后调用该类创建一个segment身段,其属性是移动海龟身段到蛇头
   坐标和将此身段对象插入列表segments首位.该类还有隐藏海龟身段方法segment_ht()供调用.
 2.游戏主循环每次循环将列表末尾元素弹出移动到蛇头的坐标后,再插到列表首位,结合1产生蛇身动画移动效果.
 3.按键盘Q键启动事件驱动,调用Screen()的专有方法bye(),终止程序运行.
 4.连续增量数除以列表含元素个数值取模(余数值),对列表切片,循环选择列表中元素,对食物海龟进行形状和颜色设置.
游戏方法:
 1.蛇头正向左或向右移动时,按键盘向上(Up)键蛇头向上移动,按向下键(Down)蛇头向下移动.
 2.蛇头正向上或向下移动时,按键盘向左(Left)键蛇头向左移动,按向右键(Right)蛇头向右移动.
 3.操作移动蛇头去碰撞食物,即吃掉食物,记分增加1分.
 4.蛇头移动时不能碰到游戏屏幕边框,如碰撞则游戏失败.
 5.蛇头移动时不能碰到蛇身体,如碰撞则游戏失败.
 6.按键盘Q键终止游戏.
认真对照这几个turtle_snake1...3版本,可学习掌握用python自带的turtle模块,编写游戏技术.
'''
import turtle #导入turtle模块,调用其对象、类和函数等前加turtle.
import time #导入time模块,调用其对象、类和函数等前加time.
import random #导入random模块,调用其对象、类和函数等前加random.

#常量设置
DISTANCE = 10 #游戏主循环每循环一次蛇头移动距离,数字越大移动速度越快蛇头部也显越大 6....20
DELAY = 0.08 #延迟时间变量设置,数字越大移动速度越慢,可调范围:0.05----0.16
FOOD_SHAPE = ["circle","square"] #设置食物海龟形态列表
FOOD_COLORS =["red","orange", "yellow", "green", "blue"] #设置食物海龟颜色列表

#变量设置
score = 0 #初始化记分变量
high_score = 0 #初始化记本次获最高分变量
segments = [] #创建并初始化蛇身各段列表
head_direction = "up" #初始化蛇头移动方向变量

#创建海龟实例对象
food = turtle.Turtle() #创建食物海龟实例对象food,调用相关函数时均要前加(food.)指明从属关系
writer = turtle.Turtle() #创建书写海龟笔实例对象writer,调用相关函数时均要前加(writer.)

#自定义蛇身各段海龟Segment类   (蛇每吃到食物后增加一个segment身段并将身段插入列表首位)
class Segment(turtle.Turtle):
    def __init__(self):
        super().__init__() #让父类Turtle的属性与子类Segment关联
        self.shape("square") #设置海龟身段形状
        self.color("grey") #设置海龟身段颜色
        self.penup() #抬起海龟身段画笔
        x=turtle.xcor() #蛇头x坐标值
        y=turtle.ycor() #蛇头y坐标值
        self.goto(x, y) #移动海龟身段到蛇头坐标
        segments.insert(0,self) #将此身段对象插入列表segments首位

    def segment_ht(self): #隐藏海龟身段方法
        self.hideturtle() #隐藏海龟身段,效果是从屏幕上删除

#自定义创建食物海龟函数,2个形参,投放食物的坐标将从这二形参数字范围内随机生成
def food_create(lowNumber,highNumber):
    global score #设置score为全局变量
    food.shape(FOOD_SHAPE[score%2]) #循环选择列表中2个形状元素.设置食物海龟形状
    food.color(FOOD_COLORS[score%5]) #循环选择列表中5个颜色元素,设置食物海龟颜色
    food.penup() #抬起海龟画笔
    # 从lowNumber到highNumber的数字中随机生成x,y
    x=random.randint(lowNumber,highNumber)
    y=random.randint(lowNumber,highNumber)
    food.goto(x,y) #食物到随机坐标位,示意新产生食物

#键盘(按上、下、左、右键)绑定的4个函数
#自定义键盘按向上键修改head_direction变量值函数
def go_up():
    global head_direction #设置head_direction为全局变量
    if head_direction != "down": #如此时蛇头正向下移动时,将不会有反应
        head_direction="up"

#自定义键盘按向下键修改head_direction变量值函数
def go_down():
    global head_direction #设置head_direction为全局变量
    if head_direction != "up": #如此时蛇头正向上移动时,将不会有反应
        head_direction="down"

#自定义键盘按向左键修改head_direction变量值函数
def go_left():
    global head_direction #设置head_direction为全局变量
    if head_direction != "right": #如此时蛇头正向右移动时,将不会有反应
        head_direction="left"

#自定义键盘按向右键修改head_direction变量值函数
def go_right():
    global head_direction #设置head_direction为全局变量
    if head_direction != "left": #如此时蛇头正向左移动时,将不会有反应
        head_direction="right"

#自定义蛇头根据head_direction变量值进行对应的方向移动函数
def move():
    global head_direction #设置head_direction为全局变量
    if head_direction == "up":
        y=turtle.ycor() #获取蛇头现y坐标
        turtle.sety(y+DISTANCE) #设蛇头y坐标为原坐标值+DISTANCE,效果为向上移动DISTANCE
    elif head_direction == "down":
        y=turtle.ycor()
        turtle.sety(y-DISTANCE) #设蛇头y坐标为原坐标值-DISTANCE,效果为向下移动DISTANCE
    elif head_direction == "left":
        x=turtle.xcor() #获取蛇头现x坐标
        turtle.setx(x-DISTANCE) #设蛇头x坐标为原坐标值-DISTANCE,效果为向左移动DISTANCE
    elif head_direction == "right":
        x=turtle.xcor()
        turtle.setx(x+DISTANCE) #设蛇头x坐标为原坐标值+DISTANCE,效果为向右移动DISTANCE

#包含有游戏主循环的游戏函数
def game():
    global head_direction,score,high_score #设置为全局变量
    turtle.onkey(None, "space") #关闭了按键盘空格键调用game()函数进行游戏
    turtle.onkeypress(go_up,"Up") #按键盘Up键调用go_up()函数
    turtle.onkeypress(go_down,"Down") #按键盘Down键调用go_down函数
    turtle.onkeypress(go_left,"Left") #按键盘Left键调用go_left函数
    turtle.onkeypress(go_right,"Right") #按键盘Right键调用go_right函数
    delay = DELAY #延迟时间变量初始化设置
    writer.clear() #清除文字
    writer_score() #调用自定义显示游戏分数文字函数
    game_on = True
    #游戏主循环  只有当 game_on = False才会退出循环,游戏终止
    while game_on:
        turtle.update() #每次循环执行一次TurtleScreen刷新
        #每次循环检测是否吃到食物,下边语句distance():返回实例turtle与food之间距离
        if turtle.distance(food)<20:
            score += 1 #记分,吃一食物加1分
            if score <=10: #在游戏初期随机范围主要在中部
                food_create(-160,160) #调自定义函数,从-160到160中随机坐标位新产生食物
            else:
                food_create(-285,285) #调自定义函数,从-285到285中随机坐标位新产生食物

            Segment() #调自定义类生成蛇身段,移动到蛇头坐标,将此对象插入列表首位
            delay -= 0.001 #减少延迟时间,表现效果为蛇移动增速
            #让变量high_score保留最高分
            if score > high_score:
                high_score = score #保留本局最高分

            writer.clear() #清除文字
            writer_score() #调用自定义显示游戏分数文字函数

        #每次游戏主循环,生成列表元素蛇身跟着蛇头移动的动画效果
        if len(segments)>0: #当列表元素个数大于0时,len(n)返回对象n的元素个数函
            x = turtle.xcor() #蛇头x坐标值
            y = turtle.ycor() #蛇头y坐标值
            end_segment = segments.pop() #弹出列表末尾元素
            end_segment.goto(x,y) #弹出列表末尾元素移动到蛇头坐标
            segments.insert(0,end_segment) #将此对象插入列表首位

        move() #调用自定义函数move(),蛇头根据head_direction值进行对应的方向产生移动

        #每次循环检查头部是否与屏幕边框碰撞
        if turtle.xcor()>290 or turtle.xcor()<-290 or turtle.ycor()>290 or turtle.ycor()<-290:
            head_direction="up" #初始化蛇头移动方向变量,此控制变量语句只能在本函数块内,否则异常
            game_on = False #退出游戏主循环,此控制变量语句只能在本函数块内,否则异常
            writer.clear() #清除文字
            writer_failed() #调用自定义显示蛇头碰撞文字函数

        #每次循环检查蛇头部是否与身体碰撞,如有身段与蛇头坐标相同即示蛇头碰撞身体
        #for i, segment in enumerate(segments): #这条语句等效下边i=0,for...,i+=1三条语句(*)
        i = 0 # *
        for segment in segments: # for循环遍历segments列表 *
            # 因吃食时它将此身段对象插入列表segments首位,故遍历判定必须从首位以后
            # 几位才开始比较,否则会误判定碰撞身体程序不能正常运行
            if i > 6: #本例为切片到segments[7]开始运行以下语句块
                 #两个及两个以上的物理行可用反斜杠（\）拼接为一个逻辑行,如下句
                if abs(segment.xcor() - turtle.xcor()) < 10 and \
                        abs(segment.ycor() - turtle.ycor()) < 10:
                #if segment.xcor() == turtle.xcor() and segment.ycor() == turtle.ycor():
                    head_direction="up" #初始化蛇头移动方向变量,此控制变量语句只能在本函数块内,否则异常
                    game_on = False #退出游戏主循环,此控制变量语句只能在本函数块内,否则异常
                    writer.clear() #清除文字
                    writer_failed() #调用自定义显示蛇头碰撞文字函数
            i += 1 # i=i+1 *

        time.sleep(delay) #每次循环调用time模块的sleep()函数,暂停delay秒调整程序执行速度

    turtle.onkeypress(None,"Up") #关闭了按键盘Up键调用go_up()函数
    turtle.onkeypress(None,"Down") #关闭了按键盘Down键调用go_down函数
    turtle.onkeypress(None,"Left") #关闭了按键盘Left键调用go_left函数
    turtle.onkeypress(None,"Right") #关闭了按键盘Right键调用go_right函数
    turtle.onkey(pre_game, "space") #按键盘空格键调用pre_game()函数

#自定义因游戏失败需重新启动游戏前期处置函数
def pre_game():
    global score,delay #设置score,delay为全局变量
    turtle.onkey(None, "space") #关闭了按键盘空格键调用pre_game()函数
    #遍历列表segments,隐藏身体部份显示
    for each in segments:
        each.segment_ht() #调用自定义蛇身各段海龟Segment类中的方法,隐藏身体段

    segments.clear() #清除列表segments全部元素
    turtle.goto(0,0) #蛇头到起点坐标
    score = 0 #初始化记分变量
    game() #调用自定义游戏主循环重启游戏

#自定义游戏运行主程序函数 main
def main():
    #global level,car_number,car_list,number
    turtle.setup(width=600, height=600) #设置游戏窗口大小
    turtle.bgcolor('#00A897') #设置游戏窗口背景颜色,颜色十六进制码的选择详见color_rgb.py
    turtle.title('A gluttonous snake.') #游戏窗口标题
    turtle.tracer(0) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(False)等效
    #初始化蛇头
    turtle.shape("square") #蛇头形状
    turtle.penup() #抬起海龟画笔
    turtle.color("black") #设置蛇头颜色
    turtle.goto(0,-100) #蛇头到起点坐标
    #初始化食物
    food_create(0,0) #调自定义函数,从0到0中随机坐标位新产生食物
    #初始化文字书写笔
    writer.penup() #抬起海龟画笔
    writer.hideturtle() #隐藏海龟
    writer_reset() #调用自定义游戏开始按键文字提示函数

    turtle.update() #执行一次TurtleScreen刷新,显示上述设置初始图像
    turtle.listen() #设置焦点接受按键亊件,下边这条语句是事件驱动(event-driven)语句
    turtle.onkey(game, "space") #按键盘空格键调用game()函数进行游戏
    turtle.onkeypress(turtle.bye,"q") #按键盘q键调用Screen()的专有方法bye(),退出程序运行
    turtle.onkeypress(turtle.bye,"Q") #按键盘Q键调用Screen()的专有方法bye(),退出程序运行
    return "turtle_snake : main() END    EVENTLOOP"

#自定义游戏开始按键文字提示函数,2个行参分别为字体中间下部位置坐标x,y
def writer_reset(x=0,y=-160):
    writer.color("#252BC3") #设置颜色,颜色十六进制码的选择详见color_rgb.py
    FONT = ("Courier", 18, "bold") #设置字体名字、字大小、字类型
    writer.goto(x,y)
    #下条隐式拼接行,圆括号、方括号、花括号内的表达式可以分成多个物理行，不必使用反斜杠\
    writer.write("Press space key to start play.",
          align="center", font=FONT) #显示出操作提示文字
    writer.goto(x,y-30)
    writer.write("Press Q key to exit.",
              align="center", font=FONT)

#自定义显示游戏分数文字函数
def writer_score():
    writer.color("white") #设置颜色
    writer.goto(0,260)
    FONT = ("Courier", 20, "normal")
    writer.write(f"Score: {score}  High Score: {high_score}",
                    align="center", font=FONT)

#自定义显示蛇头碰撞文字函数
def writer_failed():
    writer.color("red") #设置颜色
    writer.goto(0,200)
    FONT = ("Courier", 22, "normal")
    writer.write(f"Crash! Game Over.",
                    align="center", font=FONT)
    writer_score() #调用自定义显示游戏分数文字函数
    writer_reset() #调用自定义游戏开始按键文字提示函数

#程序实际执行起点
if __name__ == "__main__":   # execute only if run as a script
    msg = main()    #从这里开始执行本程序命令,调用程序主函数main()
    print(msg) #在Python shell窗口或界面打印
    turtle.mainloop()  #调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句