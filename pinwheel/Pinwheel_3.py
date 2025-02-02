'''Pinwheel_3.py 旋转风车动画  是Pinwheel_2.py的修改版本,慢速画一幅风车静态画面可观察到画图过程,并优化程序,
程序仍然是永不停动画转动(除非终断程序运行),注意与Pinwheel_2.py比较不同点.
与Pinwheel_1.py比较是另一种动画算法:定时器函数ontimer()与清屏clear()组合,以递归(函数调用身)方式,
不断画出不同旋转角度的风车画面(帧),利用人类"视觉暂留"(约0.1-0.4秒)现象构成旋转风车动画,象放映电影.
最终改写优化版详见:Pinwheel_4.py和Pinwheel_5.py.
'''
import turtle #导入turtle模块，调用其对象和函数等功能

#自创画笔不留痕迹移动到x,y位置函数
def move(x,y):
    turtle.pu() #抬起画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条,还可用penup()
    turtle.goto(x,y) #移动海龟画笔到坐标x,y
    turtle.pd() #放下画笔准备画图, 还可用down(),pendown()

#自创画一幅风车画面函数,行参degree是画这幅风车的画笔起始朝向度数
def windmill(degree):
    #画风车杆
    turtle.seth(90) #设置画笔朝向,系统默认海龟模式是standard模式,90是画笔朝向向上(北)
    turtle.pencolor('black') #设置画笔颜色
    move(0,-240) #调自创的函数,画笔不留痕迹移动0,-240
    turtle.forward(240) #画笔进前240画风车杆

    #画风车四叶片
    turtle.seth(degree) #设置画笔朝向,每一幅风车画面的起始朝向由变量degree确定
    colors = ['red','green','orange','blue'] #建立绘图所用变换的颜色列表,以便绘风车每片叶片时按列表下标取对应颜色值
    for i in range(4): #for循环4次画风车的4个叶片
        move(0,0) #调自创的函数,画笔不留痕迹移动到风车轮中心点0,0
        turtle.color(colors[i]) #设置风车叶片颜色,按颜色列表下标取每片对应颜色值
        turtle.begin_fill() #下边画图将充填颜色
        turtle.circle(40,180) #调turtle内置函数circle()绘圆：40半径,绘园时角度是180画半园
        turtle.end_fill() #在begin_fill()之间的所有绘图填色
        turtle.left(90) #画笔朝向左转90度

    #画风车叶轮中心园点
    move(0,0) #调自创的函数,画笔不留痕迹移动到风车轮中心点0,0
    turtle.dot(10,'black') #调turtle内置函数dot()绘圆点,直径10,颜色是black

#画动画风车函数 (因要使用定时器函数ontimer(),要求是无参数函数,故用全局变量来向内传递需使用的数据)
def pinwheel():
    global degree #标示degree为全局变量,变量degree是画这幅风车的画笔起始朝向度数
    turtle.clear() #删除全部绘图,清屏
    windmill(degree) #调自创风车函数,以变量degree的画笔起始朝向度数,画一幅风车
    degree += 10 #等同于degree=degree+10,每画一面风车画面后朝向转10度(增加),拟画下一幅风车
    if degree == 360: #当所画的画面旋转一周后,degree重置零而不无限增大占用内存
        degree = 0
    turtle.ontimer(pinwheel,20) #定时器函数ontimer(),调用的函数必须是无参数,本例是递归,20毫秒后调用函数自身pinwheel()

#运行本程序的自创函数简单演示部份,当本模块被其它程序导入时可自动识别而不会执行以下语句
if __name__ == "__main__": # execute only if run as a script
    #慢速画一幅风车静态画面可观察到画图过程
    turtle.speed(1) #画笔画图速度设置 1最慢,速度关系按1,2,3,4,5,6,7,8,9,0排列  最快是0
    turtle.pensize(3) #画笔粗细尺寸设置3
    turtle.bgcolor(0.5,0.5,0.5) #设置绘画窗口背景色,调色参数获取可见color_rgb.py
    windmill(0) #调用上边自创函数画一幅风车静态画面

    #风车转动动画
    turtle.hideturtle() #隐藏海龟可加速绘画速度
    turtle.tracer(False) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(0)等效
    degree = 0 #初始化全局变量,每次静态风车画面的风车角度变量
    pinwheel() #调用上边自创画风车函数实现风车旋转动画,pinwheel()无循环终止命令会无限地运行
    ###turtle.tracer(True) #在本算法不能使用恢复启用/禁用动画设置函数,如使用就无动画效果了,特在此标注提醒.
    turtle.done() #调用 Tkinter 的 mainloop 函数,必须作为一个海龟绘图程序的结束语句