# Doraemon_1.py 哆啦猫脸,最初级的绘制过程,是以turtle绘画窗口中心为基点(坐标x=0,y=0)画出图
#本程序的改进与重构可见 Doraemon_2.py和Doraemon.py
import turtle as t #创建一个turtle对象实例t

t.speed(1) #画笔画图速度设置1最慢,初学时方便观察.速度关系按1,2,3,4,5,6,7,8,9,0排列,最快是0.默认正常速度是6
# 猫脸大园
t.pensize(8) #画笔粗细尺寸设置
t.color('black','DeepSkyBlue') #设置绘制线条色black和图形内充填颜色DeepSkyBlue(十六进制颜色码#00BFFF)
t.begin_fill() #下边画图将充填颜色
t.circle(120) #调turtle内置函数circle()绘制圆：120半径,绘园时角度是黙认值360,半径值为正数画圆是反时针方向
t.end_fill() #在begin_fill()之间的所有绘图完成填色
#猫脸白色小园
t.pensize(3) #画笔粗细尺寸设置
t.fillcolor('white') #只设置图形内充填颜色,此时线条颜色同上次设定值不变
t.begin_fill()
t.circle(100) #调turtle内置函数circle()绘制圆：100半径,绘园时角度是黙认值360,半径值为正数画圆是反时针方向
t.end_fill()
#鼻子
t.pu() #抬起画笔
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(0, 134) # 移动画笔到下一个绘制图的起始位置 x=0,y=134  还可用setpos()
t.pd() #放下画笔
t.pensize(4) #画笔粗细尺寸设置
t.fillcolor("Crimson") #只设置图形内充填颜色Crimson,(十六进制颜色码#DC143C),此时线条颜色同上次设定值不变
#t.fillcolor(0.93,0.16,0.16) #只设置图形内充填颜色,此时线条颜色同上次设定值不变
t.begin_fill()
t.circle(18) #调turtle内置函数circle()绘制圆：18半径,绘园时角度是黙认值360
t.end_fill()
#鼻子中小白点鼻孔
t.pu()
t.goto(7, 155) # 移动画笔到下一个绘制图的起始位置 x=7,y=155  还可用setpos()
t.pd()
t.pensize(2) #画笔粗细尺寸设置2
t.color('white') #设置绘制线条色white和图形内充填颜色也是white
t.begin_fill()
t.circle(4) #调turtle内置函数circle()绘制圆：4半径,绘园时角度是黙认值360
t.end_fill()
#屏幕左眼圈
t.pu()
t.goto(-30, 160) #移动画笔到下一个绘制图的起始位置 x=-30,y=160  还可用setpos()
t.pd()
t.pensize(4) #画笔粗细尺寸设置4
t.color('black', 'white') #设置绘制线条色black和图形内充填颜色是white
t.begin_fill()
a = 0.4 #设置画椭园起点基数0.4
for i in range(120): #for循环画椭圆弧,从i=0开始,每循环1次i=i+1,到i=120时退出循环
    if 0 <= i < 30 or 60 <= i < 90: #画第1段或画第3段时,每次递增量
        a = a + 0.08 #在此条件下每循环1次画线的长度递增0.08
        t.lt(3)  #画笔向左转3角度,还可用left()
        t.fd(a)  #画笔按它的朝向前进变量a的值画出线条,还可用forward()
    else: #画第2段或画第4段时,每次递减量
        a = a - 0.08 #在此条件下每循环1次画线的长度递减0.08
        t.lt(3) #画笔向左转3角度,还可用left()
        t.fd(a) #画笔按它的朝向前进变量a的值画出线条,还可用forward()
t.end_fill()
#屏幕右眼圈
t.pu()
t.goto(30, 160)
t.pd()
t.color('black', 'white')
t.begin_fill()
a = 0.4 #设置画椭园起点基数0.4
for i in range(120): #for循环画椭圆弧,从i=0开始,每循环1次i=i+1,到i=120时退出循环
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.08
        t.lt(3)
        t.fd(a)
    else: #画第2段或画第4段时,每次递减量
        a = a - 0.08
        t.lt(3) #画笔向左转3角度,还可用left()
        t.fd(a)
t.end_fill()
#屏幕左眼珠
t.pu()
t.goto(-38, 190)
t.pd()
t.pensize(8)
t.lt(30) #画笔向左转30角度,还可用left()
t.forward(14)
t.right(60) #设置画笔向右转60,还可用rt()
t.forward(14)
#屏幕右眼珠
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.pu()
t.goto(22, 185)
t.pd()
t.pensize(4)
t.color('black')
t.begin_fill()
t.circle(13) #调turtle内置函数circle()绘制圆：13半径,绘园时角度是黙认值360,半径值为正数画圆是反时针方向
t.end_fill()
#屏幕右眼珠内的小白点
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.pu()
t.goto(15, 194)
t.pd()
t.pensize(2)
t.color('white')
t.begin_fill()
t.circle(5) #调turtle内置函数circle()绘制圆：5半径,绘园时角度是黙认值360,半径值为正数画圆是反时针方向
t.end_fill()
#鼻中线
t.pencolor('black') #设置画笔(画出的线条)颜色black,与color()略有区别,查手册
#t.color('black') #同上语句等效,但充填色也是black
t.pu()
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(0, 134)
t.pd()
t.right(90) #设置画笔向右转90,还可用rt()
t.pensize(4)
t.forward(40)
#屏幕右边的三根胡子
t.pensize(3)
t.pu()
t.seth(0)  #画笔朝向回到初始状态向屏幕右边 (东)
t.pd()
t.goto(0, 124)
t.left(10) #画笔向左转10角度,还可用lt()
t.forward(80)

t.pu()
t.seth(0)  #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(0, 114)
t.pd()
t.left(6) #画笔向左转6角度,还可用lt()
t.forward(80)

t.pu()
t.seth(0)  #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(0, 104)
t.pd()
t.forward(80)

# 屏幕左边的三根胡子
t.pu()
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(0, 124)
t.pd()
t.left(170)
t.forward(80)

t.pu()
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(0, 114)
t.pd()
t.left(174)
t.forward(80)

t.pu()
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(0, 104)
t.pd()
t.left(180)
t.forward(80)
#嘴巴下部弧形
t.pensize(6)
t.color('black', 'red')
t.pu()
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(-70, 70)
t.pd()
t.rt(60) #设置画笔向右转60,还可用right()
t.begin_fill()
t.circle(80, 120) #调函数circle()绘制圆：80半径,绘夹角为120的一段园弧,半径值为正数画圆是反时针方向
t.end_fill()
#嘴巴上部一横线
t.pu()
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(-80, 70)
t.pd()
t.forward(160)
#舌头上边部份
t.pensize(1)
t.fillcolor(0.97,0.47,0.16) #只设置图形内充填颜色,(十六进制颜色码#EB6E1A),此时线条颜色同上次设定值不变
t.pu()
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.goto(-50, 50)
t.pd()
t.left(40)
#t.seth(40) #
t.begin_fill()
t.circle(-40, 80)
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.left(40)
t.circle(-40, 78) #调函数circle()绘制圆：40半径,绘夹角为78的一段园弧,半径值为负数画圆是顺时针方向
#舌头下部
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.right(138)
t.circle(-76, 80) #调函数circle()绘制圆：76半径,绘夹角为80的一段园弧,半径值为负数画圆是顺时针方向
t.end_fill()
# 领带
t.pensize(14)
t.pencolor('red')
t.pu()
t.goto(-70, 12)
t.pd()
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.right(20)
t.circle(200, 40) #调函数circle()绘制圆：200半径,绘夹角为40的一段园弧,半径值为正数画圆是反时针方向
# 铃铛
t.pensize(3)
t.color("black", 'Gold')
t.pu()
t.goto(0, -46)
t.seth(0) #画笔朝向回到初始状态向屏幕右边 (东)
t.pd()
t.begin_fill()
t.circle(25)
t.end_fill()

t.pensize(2)
t.color("black","Olive" )
t.pu()
t.goto(0, -40)
t.pd()
t.begin_fill()
t.circle(5)
t.end_fill()

t.pensize(3)
t.right(115) #设置画笔向右转115,还可用rt()
t.forward(7)
t.hideturtle() #隐藏海龟隐藏画笔

t.mainloop() #还可用done(),必须作为一个海龟绘图程序的结束语句