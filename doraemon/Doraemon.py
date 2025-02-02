""" Doraemon.py 哆啦猫脸,是在Doraemon_2.py的基础改进,该模块可在绘图窗口任意坐标画出并可以被其它程序导入
-本程序要导入自建的selfTurtleModule.py模块,它应与本程序同在一个文件目录内.导入2个函数:
   1.noTraceGoto()移动画笔无移动笔迹线
   2.turtleEllips()可在turtle窗口任意坐标位置绘不同大小的椭园形
     详细说明情况请见Doraemon_2.py
-本程序创建窗口任意坐标绘哆啦猫脸图的函数doraemon(),可以被其它程序导入,有2个形参黙认值均等于0:
            X 横坐标值
            Y 垂直坐标值
-本程序结合了解Doraemon_1.py,Doraemon_2.py和selfTurtleModule.py可学习许多编程改进技巧
"""
import turtle as t #创建一个turtle对象实例t
from selfTurtleModule import noTraceGoto,turtleEllips  #从selfTurtleModule.py模块中导入2函数

def doraemon(x=0,y=0): #创建窗口任意坐标绘哆啦猫脸图的函数,可以被其它程序导入
    noTraceGoto(x,y,0) #移动海龟画笔到坐标x,y起点绘猫脸  画笔朝向0,朝屏幕右边 (东),回到初始状态
    x = t.xcor() #画图开始的画笔起点坐标x值,在原绘图横坐标点加上x值就新绘图横坐标
    y = t.ycor() #画图开始的画笔起点坐标y值,在原绘图竖坐标点加上y值就新绘图竖坐标
    t.speed(8) #画笔画图速度设置1最慢,初学时方便观察.速度关系按1,2,3,4,5,6,7,8,9,0排列,最快是0.默认正常速度是6
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
    noTraceGoto(0+x,134+y,0) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.pensize(4) #画笔粗细尺寸设置
    t.fillcolor("Crimson") #只设置图形内充填颜色Crimson,(十六进制颜色码#DC143C),此时线条颜色同上次设定值不变
    #t.fillcolor(0.93,0.16,0.16) #只设置图形内充填颜色,此时线条颜色同上次设定值不变
    t.begin_fill()
    t.circle(18) #调turtle内置函数circle()绘制圆：18半径,绘园时角度是黙认值360
    t.end_fill()
    #鼻子中小白点鼻孔
    noTraceGoto(7+x,155+y) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.pensize(2) #画笔粗细尺寸设置2
    t.color('white') #设置绘制线条色white和图形内充填颜色也是white
    t.pd()
    t.begin_fill()
    t.circle(4) #调turtle内置函数circle()绘制圆：4半径,绘园时角度是黙认值360
    t.end_fill()
    #屏幕左眼圈
    noTraceGoto(-30+x,160+y) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.pensize(4) #画笔粗细尺寸设置4
    t.color('black', 'white') #设置绘制线条色black和图形内充填颜色是white
    t.begin_fill()
    turtleEllips(3,0.4,0.08) #调用导入的画椭圆函数,初始弧线数=0.4,每笔画线增減量=0.08,每画一次画笔向左转角度=3
    t.end_fill()
    #屏幕右眼圈
    noTraceGoto(30+x,160+y) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.color('black', 'white')
    t.begin_fill()
    #turtleEllips(0.4,0.08,3) #调用导入的画椭圆函数,初始弧线数=0.4,每笔画线增減量=0.08,每画一次画笔向左转角度=3
    turtleEllips() #调用导入的画椭圆函数,初始弧线数=0.4,每笔画线增減量=0.08,每画一次画笔向左转角度=3
    t.end_fill()
    #屏幕左眼珠
    noTraceGoto(-38+x,190+y,30) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.pensize(8)
    t.forward(14)
    t.right(60) #设置画笔向右转60,还可用rt()
    t.forward(14)
    #屏幕右眼珠
    noTraceGoto(22+x,185+y,0) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.pensize(4)
    t.color('black')
    t.begin_fill()
    t.circle(13) #调turtle内置函数circle()绘制圆：13半径,绘园时角度是黙认值360,半径值为正数画圆是反时针方向
    t.end_fill()
    #屏幕右眼珠内的小白点
    noTraceGoto(15+x,194+y,0) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.pensize(2)
    t.color('white')
    t.begin_fill()
    t.circle(5) #调turtle内置函数circle()绘制圆：5半径,绘园时角度是黙认值360,半径值为正数画圆是反时针方向
    t.end_fill()
    #鼻中线
    t.pencolor('black') #设置画笔(画出的线条)颜色black,与color()略有区别,查手册
    noTraceGoto(0+x,134+y,270) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.pensize(4)
    t.forward(40)
    #屏幕右边的三根胡子
    t.pensize(3)
    noTraceGoto(0+x,124+y,10) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.forward(80)
    noTraceGoto(0+x,114+y,6) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.forward(80)
    noTraceGoto(0+x,104+y,0) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.forward(80)
    # 屏幕左边的三根胡子
    noTraceGoto(0+x,124+y,170) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.forward(80)
    noTraceGoto(0+x,114+y,174) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.forward(80)
    noTraceGoto(0+x,104+y,180) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.forward(80)
    #嘴巴下部弧形
    t.pensize(6)
    t.color('black', 'red')
    noTraceGoto(-70+x,70+y,-60) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.begin_fill()
    t.circle(80, 120) #调函数circle()绘制圆：80半径,绘夹角为120的一段园弧,半径值为正数画圆是反时针方向
    t.end_fill()
    #嘴巴上部一横线
    noTraceGoto(-80+x,70+y,0) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.forward(160)
    #舌头上边部份
    t.pensize(1)
    t.fillcolor(0.97,0.47,0.16) #只设置图形内充填颜色,(十六进制颜色码#EB6E1A),此时线条颜色同上次设定值不变
    noTraceGoto(-50+x,50+y,40) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
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
    noTraceGoto(-70+x,12+y,340) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.circle(200, 40) #调函数circle()绘制圆：200半径,绘夹角为40的一段园弧,半径值为正数画圆是反时针方向
    # 铃铛
    t.pensize(3)
    t.color("black", 'Gold')
    noTraceGoto(0+x,-46+y,0) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.pensize(2)
    t.color("black","Olive" ) # Olive十六进制颜色码#808000
    noTraceGoto(0+x,-40+y,0) #无痕迹移动画笔,在原绘图横坐标点加上x值,竖坐标点加上y值就新绘图坐标
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.pensize(3)
    t.right(115) #设置画笔向右转115,还可用rt()
    t.forward(7)
#运行简单演示部份,当本模块被其它程序导入时可自动识别而不会执行以下语句
if __name__ == "__main__":   # execute only if run as a script,模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行下边代码，而在被 import 时不会执行
    t.tracer(0)     #加速画图设置，画复杂图形很快很快,可前加#注释不执行,画得慢而便于观察
    doraemon(-158,56) #调用doraemon()函数在坐标x=-158,y=56起点位画哆啦猫脸
    doraemon(0,0) #调用doraemon()函数在坐标x=0,y=0起点位,也是Doraenon_2.py的基点坐标所画的哆啦猫脸
    doraemon(180,-220) #调用doraemon()函数在坐标x=180,y=-220起点位画哆啦猫脸
    t.tracer(1)     #将前更改值0设置回到原黙认值1,否则会出现最后图形漏末尾笔画
    t.hideturtle() #隐藏海龟隐藏画笔,便于看哆啦猫脸
    t.mainloop() #还可用done(),必须作为一个海龟绘图程序的结束语句