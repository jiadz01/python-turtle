'''Pinwheel_5.py 旋转风车动画  是Pinwheel_1.py的重写优化版本 2021.09.21
可在任意坐标先慢速画一幅风车静态画面，观察画图过程.
可通过函数形参设置风车坐标位置和旋转圈数(程序可在旋转设定圈数后自动停止运行),还可设置风车旋转方向(正或反时针).
rotateWindmill_5()动画主函数可被其它程序导入调用(只能运行1次),详见:Pinwheel_6.py
采用动画算法:定时器函数ontimer()与清屏clear()组合,以递归(函数调用身)方式,
不断画出不同旋转角度的风车画面(帧),利用人类"视觉暂留"(约0.1-0.4秒)现象构成旋转风车动画.
这个动画组合只能在程序中最后边1次调用执行,后边的语句无效并不能正常运行!
自定义4个绘画函数:
- move()函数,无移动笔迹线移动画笔,有2个形参:
        X 横坐标值
        Y 垂直坐标值

- windmill()函数,画一幅风车,有3个形参,黙认值均等于0:
        X 风车横坐标值
        Y 风车垂直坐标值
        degree 风车的画笔起始朝向度数

- pinwheel()函数,画动画风车,因要使用定时器函数ontimer(),要求是无参数函数:
           用全局变量 x0,y0,degree,turn0,z,direction0来向内传递需使用的数据

- rotateWindmill_5()函数,动画主函数,有4个形参:
        X 风车横坐标值,黙认值=0
        Y 风车垂直坐标值,黙认值=0
        turn 整数参数,设定画动旋转圈数,黙认值=6
        direction 布尔变量参数,风车旋转方向,值是False(黙认值)反时针旋转,True顺时针旋转
另有详见:Pinwheel_4.py,Pinwheel_6.py
'''
import turtle #导入turtle模块，调用其对象和函数等功能前加(turtle.)

#自创画笔不留痕迹移动到x,y位置函数
def move(x,y):
    turtle.pu() #抬起画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条,还可用penup()
    turtle.goto(x,y) #移动海龟画笔到坐标x,y
    turtle.pd() #放下画笔准备画图, 还可用down(),pendown()

#自创画一幅风车画面函数,行参x,y画风车的坐标位置,degree是画这幅风车的画笔起始朝向度数
def windmill(x=0,y=0,degree=0):
    #画风车杆
    turtle.pensize(6) #画笔粗细尺寸设置6
    turtle.pencolor('green') #设置画笔颜色
    turtle.seth(90) #设置画笔朝向,系统默认海龟模式是standard模式,90是画笔朝向向上(北)
    move(x,y-180) #调自创的函数,画笔不留痕迹移动x,y-180
    turtle.forward(180) #画笔进前180画风车杆

    #画风车四叶片
    turtle.pensize(1) #画笔粗细尺寸设置1
    turtle.pencolor('blue') #设置画笔颜色
    turtle.seth(degree) #设置画笔朝向,每一幅风车画面的起始朝向由变量degree确定
    for i in range(4): #for循环4次画风车四个叶片,i=0,1,2,3
        move(x,y) #调自创的函数,画笔不留痕迹移动到风车轮中心点x,y
        turtle.fillcolor('#50B2F8') #设置叶片前端充填颜色
        turtle.begin_fill() #下边画图将充填颜色
        turtle.forward(100) #画笔前进100画出线条
        turtle.left(150) #设置画笔向左转150角度值
        turtle.forward(70) #画笔前进70画出线条
        turtle.end_fill() #在begin_fill()之间的叶片前端绘图完成填色
        turtle.fillcolor('#063EC5') #设置叶片后段充填颜色
        turtle.begin_fill() #下边画图将充填颜色
        turtle.left(30) #设置画笔向左转30角度值
        turtle.forward(40) #画笔前进40画出线条
        turtle.left(90) #设置画笔向左转90角度值
        turtle.forward(35) #画笔前进35画出线条
        turtle.end_fill() #在begin_fill()之间的叶片后段绘图完成填色
        #以上刚画完风车一片叶片,画笔回到起始点,画笔朝向正好适合画下一叶片

    #画风车叶轮中心园点
    move(x,y) #调自创的函数,画笔不留痕迹移动到风车轮中心点0,0
    turtle.dot(18,'green') #调turtle内置函数dot()绘圆点,直径16,颜色是cyan


#画动画风车函数,因要使用定时器函数ontimer(),要求是无参数函数,用全局变量来向内传递需使用的数据
def pinwheel():
    global x0,y0,degree,turn0,z,direction0 #标示x0,y0,degree,turn0,z,direction0为全局变量
    turtle.clear() #删除全部绘图,清屏
    windmill(x0,y0,degree) #调用上边自创函数画一幅(帧)风车静态画面

    if direction0 == True: #旋转方向布尔变量direction=True动画顺时针旋转,否则动画反时针旋转
        degree -= 10 #等效degree=degree-10,画下一幅(帧)风车静态画面的画笔朝向减少10度,负数角度值动画顺时针旋转
    else: #否则动画反时针旋转
        degree += 10 #等效degree=degree+10,画下一幅(帧)风车静态画面的画笔朝向增加10度,正数角度值动画反时针旋转

    if abs(degree) == 360: #abs()求degree绝对值,当变量degree绝对值等于360即画完风车旋转1圈
        degree = 0 #角度重置为零,以便计算下1圈
        z += 1 #即是z=z+1,变量z是动画风车已旋转次数

    if z <= turn0: #只有风车旋转圈数小于或等于设定置时才能执行以下递归语句
        turtle.ontimer(pinwheel,20) #定时器函数ontimer(),调用的函数必须是无参数,本例是递归
                                    #20毫秒后调用函数自身pinwheel()


#动画主函数,有4个形参,以6个全局变量向无参数pinwheel()函数传递需使用的数据
def rotateWindmill_5(x=0,y=0,turn=6,direction=False):
    global x0,y0,degree,turn0,z,direction0 #标示x0,y0,degree,turn0,z,direction0为全局变量
    z = 1 #初始化旋转次数变量z,全局变量
    degree = 0 #初始化风车画启始点画笔朝向角度值,全局变量
    turn0 = turn #全局变量,设定画动旋转圈数,
    direction0 = direction #全局变量
    x0 = x #全局变量,风车横坐标值
    y0 = y #全局变量,风车垂直坐标值
    turtle.hideturtle() #隐藏海龟可加速绘画速度
    turtle.tracer(0) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(False)等效
    pinwheel() #调用上边自创画动画风车函数

#运行本程序的自创函数调用演示部份,当本模块被其它程序导入时可自动识别而不会执行以下语句，可改变参数调用观看不同的动画效果
if __name__ == "__main__": # execute only if run as a script
    #慢速画风车静态画面,可观察到画图过程
    turtle.speed(1) #画笔画图速度设置 1最慢,速度关系按1,2,3,4,5,6,7,8,9,0排列  最快是0
    turtle.bgcolor(0.5,0.5,0.5) #设置绘画窗口背景色,调色参数获取可见color_rgb.py
    windmill(0,0,0) #调用上边自创函数画风车静态画面,风车中心坐标位和朝向角度值等这三个参数可自由设定

    #风车旋转动画,只能正确执行下边1条语句,其余要去掉或用#注释掉,可选择其中1条执行看效果
    rotateWindmill_5(0,0,3,True) #调用上边自创函数在x=0,y=0坐标动画风车,顺时针旋转3圈
    #rotateWindmill_5(80,60,6) #调用上边自创函数在x=80,y=60坐标动画风车,反时针旋转6圈

    turtle.done() #调用 Tkinter 的 mainloop 函数,必须作为一个海龟绘图程序的结束语句,还可用mainloop()