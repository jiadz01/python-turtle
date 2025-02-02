'''PeppaPig_4.py 佩奇小猪  在PeppaPig_3.py程序基础上另外一种方式改写.
本程序要导入自建的self_module.py模块,它应与本程序同在一个文件目录内,导入2个函数:
    1.根据画笔朝向和袳动步数来移动画笔不留笔迹线条函数:move(),
    2.画椭园形函数:turtleEllips().
    注意这些导入的函数与selfTurtleModule.py模块的同名函数在调用方式是有区别的!
本程序要导入自建的selfTurtleModule.py模块,它应与本程序同在一个文件目录内,导入1个绘画函数:
    画海龟坐标图函数:coordinate().

自定义1个绘画函数:
- peppapig()函数,可在turtle窗口任意坐标位置绘佩奇小猪,可供其它程序导入调用,有3个行参：
        turtle调用该函数的对象(实例)或称画笔
        X 横坐标值,黙认值=0
        Y 垂直坐标值,黙认值=0
认真分析、比较PeppaPig_n.py这一系列5个佩奇小猪程序的变化,可了解和学习一些编程技巧.
'''
import turtle #导入turtle模块，调用其对象和函数等功能
from self_module import move,turtleEllips  #从self_module.py模块中导入2个绘画函数
from selfTurtleModule import coordinate  #从selfTurtleModule.py模块中导入coordinate()绘画坐标函数,

pen = turtle.Turtle() #创建一个turtle对象实例pen

#定义画佩奇小猪函数,有3个形参
def peppapig(turtle,x=0,y=0):
    turtle.pensize(4) #画笔粗细尺寸设置4
    turtle.color((1.0,0.61,0.76),"pink") #设置绘制线条色(1.0,0.61,0.76  颜色RGB模式1.0的值)和图形内充填颜色pink
    # 画鼻子  鼻孔处的椭园形
    turtle.pu() # 抬起画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条,还可用penup(),up()
    turtle.goto(x-100,y+100)  # 移动海龟画笔到坐标x-100,y+100位置准备绘图,定位图形初始坐标位
    turtle.pd() # 放下画笔准备画图, 还可用pendown() ; down()
    turtle.seth(-30) #将画笔朝向转到-30(负数即顺时针方向)角度位,还可用setheading()
    turtle.begin_fill() #下边画图将充填颜色
    turtleEllips(turtle) #调自定义的画椭园形函数,画鼻孔处的椭园形,等效语句turtleEllips(3,0.4,0.08,360)
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    #画鼻孔  左边鼻孔
    turtle.fillcolor(0.63,0.32,0.18) #设置绘制图形内充填颜色(0.63,0.32,0.18  颜色RGB模式1.0的值)
    move(turtle,90,25,0,8) #无笔迹移到画左边鼻孔起始点,放下画笔准备画图
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(5) #左边鼻孔,反时针绘制圆：半径=5,绘园时角度是黙认值360,画完园后画笔回到启始点
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    #右边鼻孔
    move(turtle,0,18) #无笔迹移到画右边鼻孔起始点,放下画笔准备画图,后边2个参数省略即取默认值全为零
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(5) #右边鼻孔,反时针绘制圆：半径=5,绘园时角度是黙认值360,画完园后画笔回到启始点
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    # 绘头面部
    turtle.color((1.0,0.61,0.76),"pink") #设置绘制线条色(1.0,0.61,0.76  颜色RGB模式1.0的值)和图形内充填颜色pink
    move(turtle,90,41,0,3) #无笔迹移到画头面部起始点,放下画笔准备画图
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(-300, 30) #绘制圆弧线：半径=300,负数即是顺时针方向绘画,弧度=30
    turtle.circle(-100, 60) #接着上条弧线终点绘制圆弧线：半径=100,负数即是顺时针方向绘画,弧度=60
    turtle.circle(-82, 100) #接着上条弧线终点绘制圆弧线：半径=82,负数即是顺时针方向绘画,弧度=100
    turtle.circle(-150, 20) #接着上条弧线终点绘制圆弧线：半径=150,负数即是顺时针方向绘画,弧度=20
    turtle.circle(-60, 95) #接着上条弧线终点绘制圆弧线：半径=60,负数即是顺时针方向绘画,弧度=95
    turtle.pu() #抬起画笔,移动画笔不留笔迹线条
    turtle.goto(x-100,y+100) # 移动海龟画笔到坐标x-100,y+100位置,到前边画鼻子的椭园形起始点
    turtle.pd() #放下画笔准备画图
    turtle.seth(-30) #将画笔朝向转到-30(负数即顺时针方向)角度位
    turtleEllips(turtle,3,0.4,0.08,180) #调自定义的画椭园形函数,重描上面已画好的椭园形一半,以便头部填充颜色完整正确
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    # 耳朵  画面左边耳朵
    turtle.color((1.0,0.61,0.76),"pink") #设置绘制线条色(1.0,0.61,0.76  颜色RGB模式1.0的值)和图形内充填颜色pink
    move(turtle,90,-7,0,70) #无笔迹移到画左边耳朵起始点,放下画笔准备画图
    turtle.seth(100) #将画笔朝向转到100角度位,向上稍偏左点
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(-50,50) #绘制圆弧线：半径=50,负数即是顺时针方向绘画,弧度=50
    turtle.circle(-10,120) #接着上条弧线终点绘制圆弧线：半径=10,负数即是顺时针方向绘画,弧度=120
    turtle.circle(-50,54) #接着上条弧线终点绘制圆弧线：半径=50,负数即是顺时针方向绘画,弧度=54
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    #画面右边耳朵
    move(turtle,270,12,0,30) #无笔迹移到画右边耳朵起始点,放下画笔准备画图
    turtle.seth(90) #将画笔朝向转到90角度位,向上
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(-50,50) #绘制圆弧线：半径=50,负数即是顺时针方向绘画,弧度=50
    turtle.circle(-10,120) #接着上条弧线终点绘制圆弧线：半径=10,负数即是顺时针方向绘画,弧度=120
    turtle.circle(-50,54) #接着上条弧线终点绘制圆弧线：半径=50,负数即是顺时针方向绘画,弧度=54
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    # 眼睛  画面左边眼睛
    turtle.color((1.0,0.61,0.76),"white") #设置绘制线条色(1.0,0.61,0.76  颜色RGB模式1.0的值)和图形内充填颜色white
    move(turtle,270,20,0,-95) #无笔迹移到起始点,准备画左边眼睛
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(15) #绘制圆：半径=15,正数即是反时针方向绘画
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    #画面左边眼珠
    turtle.color("black") #设置绘制线条色和图形内充填颜色black
    move(turtle,90,12,0,-3) #无笔迹移到起始点,准备画左边眼珠
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(3) #绘制圆：半径=3,正数即是反时针方向绘画
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    #画面右边眼睛
    turtle.color((1.0,0.61,0.76),"white") #设置绘制线条色(1.0,0.61,0.76  颜色RGB模式1.0的值)和图形内充填颜色white
    move(turtle,270,25,0,40) #无笔迹移到起始点,准备画右边眼睛
    turtle.begin_fill()#下边画图将充填颜色
    turtle.circle(15) #绘制圆：半径=15,正数即是反时针方向绘画
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    #画面右边眼珠
    turtle.color("black") #设置绘制线条色和图形内充填颜色black
    move(turtle,90,12,0,-3) #无笔迹移到起始点,准备画右边眼珠
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(3) #绘制圆：半径=3,正数即是反时针方向绘画
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    # 画腮帮子
    turtle.color((1.0,0.61,0.76)) #设置绘制线条色和图形内充填颜色(1.0,0.61,0.76  颜色RGB模式1.0的值)
    move(turtle,270,95,0,65) #无笔迹移到画腮帮子起始点,放下画笔准备画图
    turtle.begin_fill() #下边画图将充填颜色
    turtle.circle(30) #绘制圆：半径=30,正数即是反时针方向绘画
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    # 画嘴巴
    turtle.color(0.94,0.27,0.08) #设置绘制线条色和图形内充填颜色(0.94,0.27,0.08  颜色RGB模式1.0的值)
    move(turtle,90,15,180,100) #无笔迹移到起始点,准备画画嘴巴,放下画笔准备画图
    turtle.seth(-80) #将画笔朝向转到-80(负数即顺时针方向)角度位，等效用seth(280)
    turtle.circle(40,120) #绘制圆弧线：半径=40,正数即是反时针方向绘画,弧度=120,画嘴巴
    # 画身体
    turtle.color("red",(1.0,0.39,0.28))  #设置绘制线条色red和图形内充填颜色(1.0,0.39,0.28  颜色RGB模式1.0的值)
    move(turtle,270,20,180,78) #无笔迹移到画身体始点,放下画笔准备画图
    turtle.begin_fill() #下边画图将充填颜色
    turtle.seth(230) #将画笔朝向转到230角度位,向下偏左
    turtle.circle(100,10) #绘制圆弧线：半径=100,正数即是反时针方向绘画,弧度=10
    turtle.circle(300,30) #接着上条弧线终点绘制圆弧线：半径=300,正数即是反时针方向绘画,弧度=30
    turtle.seth(0) #将画笔朝向转到0角度位,向右
    turtle.fd(230) #向右移动230,绘直线
    turtle.seth(90) #将画笔朝向转到90角度位,向上
    turtle.circle(300,30) #绘制圆弧线：半径=300,正数即是反时针方向绘画,弧度=30
    turtle.circle(100,7) #接着上条弧线终点绘制圆弧线：半径=100,正数即是反时针方向绘画,弧度=7
    turtle.color((1.0,0.61,0.76),(1.0,0.39,0.39)) #设置绘制线条色(1.0,0.61,0.76)和图形内充填颜色(1.0,0.39,0.39  颜色RGB模式1.0的值)
    turtle.seth(225) #将画笔朝向转到225角度位,向下偏左
    turtle.circle(-80,63) #绘制圆弧线：半径=80,负数即是顺时针方向绘画,弧度=63
    turtle.circle(-150,24) #接着上条弧线终点绘制圆弧线：半径=150,负数即是顺时针方向绘画,弧度=24
    turtle.end_fill() #在begin_fill()之间的所有绘图完成填色
    # 画手  画左边手
    turtle.color((1.0,0.61,0.76)) #设置绘制线条色和图形内充填颜色(1.0,0.61,0.76  颜色RGB模式1.0的值)
    move(turtle,270,40,180,20) #无笔迹移到画左边手起始点,放下画笔准备画图
    turtle.seth(200) #将画笔朝向转到200角度位,向左偏下
    turtle.circle(300,15) #绘制圆弧线：半径=300,正数即是反时针方向绘画,弧度=15
    move(turtle,90,15) #无笔迹移到起始点,放下画笔准备画图
    turtle.seth(-10) #将画笔朝向转到-10(负数即顺时针方向)角度位，等效用seth(350),向右偏下
    turtle.circle(-20,90) #绘制圆弧线：半径=20,负数即是顺时针方向绘画,弧度=90
    #画右边手
    move(turtle,90,31,0,234) #无笔迹移到画右边手起始点,放下画笔准备画图
    turtle.seth(-20) #将画笔朝向转到-20(负数即顺时针方向)角度位，等效用seth(340),向右偏下
    turtle.circle(-300,15) #绘制圆弧线：半径=300,负数即是顺时针方向绘画,弧度=15
    move(turtle,90,18) #无笔迹移到起始点,放下画笔准备画图
    turtle.seth(190) #将画笔朝向转到190角度位,向左稍偏下
    turtle.circle(20,90) #绘制圆弧线：半径=20,正数即是反时针方向绘画,弧度=90
    #画脚  画左边脚
    turtle.pensize(10) #画笔粗细尺寸设置10
    turtle.color((0.94,0.5,0.5)) #设置绘制线条色和图形内充填颜色(0.94,0.5,0.5  颜色RGB模式1.0的值)
    move(turtle,270,81,180,180) #无笔迹移到画左边脚起始点,放下画笔准备画图
    turtle.seth(270) #将画笔朝向转到270角度位,向下
    turtle.fd(40) #向下移动40，画线条
    turtle.seth(180) #将画笔朝向转到180角度位,向左
    turtle.color("black") #设置绘制线条色和图形内充填颜色black
    turtle.pensize(15) #画笔粗细尺寸设置15
    turtle.fd(20) #向左移动20，画线条
    #画右边脚
    turtle.pensize(10) #画笔粗细尺寸设置10
    turtle.color((0.94,0.5,0.5)) #设置绘制线条色和图形内充填颜色(0.94,0.5,0.5  颜色RGB模式1.0的值)
    move(turtle,90,40,0,90) #无笔迹移到画右边脚起始点,放下画笔准备画图
    turtle.seth(270) #将画笔朝向转到270角度位,向下
    turtle.fd(40) #向下移动40，画线条
    turtle.seth(180) #将画笔朝向转到180角度位,向左
    turtle.color("black") #设置绘制线条色和图形内充填颜色black
    turtle.pensize(15) #画笔粗细尺寸设置15
    turtle.fd(20) #向左移动20，画线条
    # 画尾巴
    turtle.pensize(4) #画笔粗细尺寸设置4
    turtle.color((1.0,0.61,0.76)) #设置绘制线条色和图形内充填颜色(1.0,0.61,0.76  颜色RGB模式1.0的值)
    move(turtle,90,72,0,98) #无笔迹移到画尾巴起始点,放下画笔准备画图
    turtle.circle(70,20) #绘制圆弧线：半径=70,正数即是反时针方向绘画,弧度=20
    turtle.circle(10,330) #接着上条弧线终点绘制圆弧线：半径=10,正数即是反时针方向绘画,弧度=330
    turtle.circle(70,30) #接着上条弧线终点绘制圆弧线：半径=70,正数即是反时针方向绘画,弧度=30

#运行简单演示部份,当本模块被其它程序导入时可自动识别而不会执行以下语句
if __name__ == "__main__":   # execute only if run as a script,模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行下边代码，而在被 import 时不会执行
    coordinate() #绘出turtle绘画窗口默认标准坐标线,可用#注释掉,不执行
    pen.speed(3) # 画笔pen画图速度设置,速度关系按1,2,...,9,0排列,1最慢(初学时方便观察),最快是0,可据自已要求修改
    turtle.speed(0) # 画笔turtle画图速度设置
    #turtle.tracer(0)     #加速画图设置，画复杂图形很快很快,可前加#注释不执行,画得慢而便于观察
    peppapig(pen,-230,-80) #画笔pen调用画佩奇小猪函数在x=-230,y=-80坐标画图
    peppapig(turtle,130,100) #画笔turtle调用画佩奇小猪函数在x=130,y=100默认坐标画图
    turtle.tracer(1)     #将前更改值0设置回到原黙认值1,否则会出现最后图形漏末尾笔画
    pen.hideturtle() #隐藏海龟画笔pen
    turtle.mainloop() #还可用done(),必须作为一个海龟绘图程序的结束语句