""" Doraemon_2.py 哆啦猫脸,是在Doraemon_1.py的基础改进,主要是导入自编模块中的部份函数以优化本程序并更简洁
本程序要导入自建的selfTurtleModule.py模块,它应与本程序同在一个文件目录内.导入如下函数:
- noTraceGoto()函数,移动画笔无移动笔迹线,每次移动后笔的朝向转到设置的角度或回到初始朝向,有3个形参黙认值均等于0:
    X 横坐标值  Y 垂直坐标值  angle 画笔朝向的角度,整型或浮点型
- turtleEllips()函数,可在turtle窗口任意坐标位置绘不同大小的椭园形,有3个行参：
            initial浮点数参数,椭圆初始弧线数,取值范围0.1 - 8,黙认值0.4,值越大图形越大,也渐由椭园变成园形
            idquantity浮点数参数,每笔画线增減量,取值范围0.02 - 0.6,黙认值0.08,值越大椭圆越长越大
            angle浮点数参数,每画一次画笔向左转角度值,取值范围1.5 - 4,黙认值3,值越大椭圆小,值越小椭圆大
                initial和angle的值都越小,画出的椭圆越大也越椭(越长),所有参数都应在取值范围内！
- coordinate()函数,无参数,自动绘出turtle绘画窗口默认标准坐标线,可观察和学习绘图窗口坐标值的选取
本程序的重构和最终模块是Doraemon.py,该模块可在turtle绘图窗口任意坐标画出并可以被其它程序导入使用.
"""
import turtle as t #创建一个turtle对象实例t
from selfTurtleModule import coordinate,noTraceGoto,turtleEllips  #从selfTurtleModule.py模块中导入3函数

coordinate() #画出海龟坐标图，便于绘图时理解坐标定义,可前边加#注释掉不执行
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
noTraceGoto(0,134,0) #无痕迹移动画笔x=0,y=134,画笔朝向0,朝屏幕右边 (东),回到初始状态
t.pensize(4) #画笔粗细尺寸设置
t.fillcolor("Crimson") #只设置图形内充填颜色Crimson,(十六进制颜色码#DC143C),此时线条颜色同上次设定值不变
#t.fillcolor(0.93,0.16,0.16) #只设置图形内充填颜色,此时线条颜色同上次设定值不变
t.begin_fill()
t.circle(18) #调turtle内置函数circle()绘制圆：18半径,绘园时角度是黙认值360
t.end_fill()
#鼻子中小白点鼻孔
noTraceGoto(7,155) #无痕迹移动画笔x=7,y=155,画笔朝向黙认值=0,朝屏幕右边 (东),回到初始状态
t.pensize(2) #画笔粗细尺寸设置2
t.color('white') #设置绘制线条色white和图形内充填颜色也是white
t.pd()
t.begin_fill()
t.circle(4) #调turtle内置函数circle()绘制圆：4半径,绘园时角度是黙认值360
t.end_fill()
#屏幕左眼圈
noTraceGoto(-30,160) #无痕迹移动画笔x=-30,y=160,画笔朝向黙认值=0,朝屏幕右边 (东),回到初始状态
t.pensize(4) #画笔粗细尺寸设置4
t.color('black', 'white') #设置绘制线条色black和图形内充填颜色是white
t.begin_fill()
turtleEllips(3,0.4,0.08) #调用导入的画椭圆函数,初始弧线数=0.4,每笔画线增減量=0.08,每画一次画笔向左转角度=3
t.end_fill()
#屏幕右眼圈
noTraceGoto(30,160) #无痕迹移动画笔x=30,y=160,画笔朝向黙认值=0,朝屏幕右边 (东),回到初始状态
t.color('black', 'white')
t.begin_fill()
turtleEllips(3,0.4,0.08) #调用导入的画椭圆函数,初始弧线数=0.4,每笔画线增減量=0.08,每画一次画笔向左转角度=3
t.end_fill()
#屏幕左眼珠
noTraceGoto(-38,190,30) #无痕迹移动画笔x=-38,y=190,画笔朝向30角度
t.pensize(8)
t.forward(14)
t.right(60) #设置画笔向右转60,还可用rt()
t.forward(14)
#屏幕右眼珠
noTraceGoto(22,185,0) #无痕迹移动画笔x=22,y=185,画笔朝向黙认值=0,朝屏幕右边 (东),回到初始状态
t.pensize(4)
t.color('black')
t.begin_fill()
t.circle(13) #调turtle内置函数circle()绘制圆：13半径,绘园时角度是黙认值360,半径值为正数画圆是反时针方向
t.end_fill()
#屏幕右眼珠内的小白点
noTraceGoto(15,194,0) #无痕迹移动画笔x=15,y=194,画笔朝向=0,朝屏幕右边 (东),回到初始状态
t.pensize(2)
t.color('white')
t.begin_fill()
t.circle(5) #调turtle内置函数circle()绘制圆：5半径,绘园时角度是黙认值360,半径值为正数画圆是反时针方向
t.end_fill()
#鼻中线
t.pencolor('black') #设置画笔(画出的线条)颜色black,与color()略有区别,查手册
#t.color('black') #同上语句等效,但充填色也是black
noTraceGoto(0,134,270) #无痕迹移动画笔x=0,y=134,画笔朝向270,朝屏幕下边 (南),还可用-90右转90
t.pensize(4)
t.forward(40)
#屏幕右边的三根胡子
t.pensize(3)
noTraceGoto(0,124,10) #无痕迹移动画笔x=0,y=124,画笔朝向10,朝屏幕右边偏向上
t.forward(80)
noTraceGoto(0,114,6) #无痕迹移动画笔x=0,y=114,画笔朝向6,朝屏幕右边偏向上
t.forward(80)
noTraceGoto(0,104,0) #无痕迹移动画笔x=0,y=104,画笔朝向=0,朝屏幕右边 (东),回到初始状态
t.forward(80)
# 屏幕左边的三根胡子
noTraceGoto(0,124,170) #无痕迹移动画笔x=0,y=124,画笔朝向170,朝屏幕左边偏向上
t.forward(80)
noTraceGoto(0,114,174) #无痕迹移动画笔x=0,y=114,画笔朝向174,朝屏幕左边偏向上
t.forward(80)
noTraceGoto(0,104,180) #无痕迹移动画笔x=0,y=104,画笔朝向180,朝屏幕左边
t.forward(80)
#嘴巴下部弧形
t.pensize(6)
t.color('black', 'red')
noTraceGoto(-70,70,-60) #无痕迹移动画笔x=-70,y=70,画笔朝向-60,角度值为负数画笔朝向是顺时针方向转,还可用是300相同朝向
#noTraceGoto(-70,70,300) #无痕迹移动画笔x=-70,y=70,画笔朝向300,角度值为正数画笔朝向是反时针方向转,还可用是-60相同朝向
t.begin_fill()
t.circle(80, 120) #调函数circle()绘制圆：80半径,绘夹角为120的一段园弧,半径值为正数画圆是反时针方向
t.end_fill()
#嘴巴上部一横线
noTraceGoto(-80,70,0) #无痕迹移动画笔x=-80,y=70,画笔朝向=0,朝屏幕右边 (东),回到初始状态
t.forward(160)
#舌头上边部份
t.pensize(1)
t.fillcolor(0.97,0.47,0.16) #只设置图形内充填颜色,(十六进制颜色码#EB6E1A),此时线条颜色同上次设定值不变
noTraceGoto(-50,50,40) #无痕迹移动画笔x=-50,y=50,画笔朝向40,朝屏幕左边偏向上,角度值为正数画笔朝向是反时针转
t.begin_fill()
t.circle(-40, 80)
t.seth(40) #画笔指向角度40,回到前画弧起点朝向
t.circle(-40, 78) #调函数circle()绘制圆：40半径,绘夹角为78的一段园弧,半径值为负数画圆是顺时针方向
#舌头下部
t.seth(222) #画笔指向角度222,还可用负数-138设置,画笔指向角度相同
t.circle(-76, 80) #调函数circle()绘制圆：76半径,绘夹角为80的一段园弧,半径值为负数画圆是顺时针方向
t.end_fill()
# 领带
t.pensize(14)
t.pencolor('red')
noTraceGoto(-70,12,340) #无痕迹移动画笔x=-70,y=12,画笔朝向340,还可用负数-20设置,画笔指向角度相同
#noTraceGoto(-70,12,-20) #无痕迹移动画笔x=-70,y=12,画笔朝向-20,还可用正数340设置,画笔指向角度相同
t.circle(200, 40) #调函数circle()绘制圆：200半径,绘夹角为40的一段园弧,半径值为正数画圆是反时针方向
# 铃铛
t.pensize(3)
t.color("black", 'Gold')
noTraceGoto(0,-46,0) #无痕迹移动画笔x=0,y=-46,画笔朝向0,初始状态向屏幕右边 (东)
t.begin_fill()
t.circle(25)
t.end_fill()

t.pensize(2)
t.color("black","Olive" ) # Olive十六进制颜色码#808000
noTraceGoto(0,-40,0) #无痕迹移动画笔x=0,y=-40,画笔朝向0,初始状态向屏幕右边 (东)
t.begin_fill()
t.circle(5)
t.end_fill()

t.pensize(3)
t.right(115) #设置画笔向右转115,还可用rt()
t.forward(7)
t.hideturtle() #隐藏海龟隐藏画笔
#coordinate() #再次画出海龟坐标图，便于绘图时理解坐标定义,可前边加#注释掉不执行

t.mainloop() #还可用done(),必须作为一个海龟绘图程序的结束语句