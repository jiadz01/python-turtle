""" self_module.py  可供其它程序导入调用的自编8个绘画函数模块,是selfTurtleModule.py的另一种版本:
  所有绘画函数都在形参第一位增加一个turtle参数変量,便于程序中多个(区分)不同对象实例调用该函数.
自定义8个绘画函数: (最后修订日期:2021.10.6)
- turtleStar()函数,可在turtle窗口任意坐标位置绘图.可绘多种图型,有6个形参:
             turtle调用该函数的对象(实例)
             length整数参数,绘图时每边(直线)长度值
             corner整数参数,每绘完一边后画笔转向的角度数值,
                (角度值=144是五角星,角度值=120是三角形,角度值=90是正方形,角度值=170是海龟星)
             turn字符串参数,笔旋转方向,'left'向左(黙认值)转,'right'向右转
             coloring布尔变量参数,值是True时所绘图形,不充填颜色是False(黙认值)
             stamp布尔变量参数,值是True时所绘图形起点留下画笔印章,False(黙认值)不留下画笔印章

- noTraceGoto()函数,移动画笔无移动笔迹线,每次移动后笔的朝向转到设置的角度或回到初始朝向,有4个形参黙认值均等于0:
             turtle调用该函数的对象(实例)
             X 横坐标值
             Y 垂直坐标值
             angle 画笔朝向的角度,整型或浮点型

- move()函数,根据画笔朝向和袳动步数来移动画笔不留笔迹线条,有5个形参:
             turtle调用该函数的对象(实例)
             angle1画笔朝向1
             step1袳动步数1,负数为后退
             angle2画笔朝向2,黙认值=0(标准模式是向右)
             step1袳动步数2,负数为后退,黙认值=0

- turtleEllips()函数,可在turtle窗口任意坐标位置绘不同大小的椭园形,有5个行参：
            turtle调用该函数的对象(实例)
            angle浮点数参数,每画一次画笔向左转角度值,取值范围1.50- 4.0,黙认值3,值越大椭圆小,值越小椭圆大
            initial浮点数参数,椭圆初始弧线数,取值范围0.1 - 8,黙认值0.4,值越大图形越大,也渐由椭园变成园形
            idquantity浮点数参数,每笔画线增減量,取值范围0.02 - 0.6,黙认值0.08,值越大椭圆越长越大
            radian 椭圆弧度值,取值范围10 - 360,黙认值360椭园形
                initial和angle的值都越小,画出的椭圆越大也越椭(越长),所有参数都应在取值范围内！

- waveformGraph_x()函数,画波形图函数,沿X轴水平方向,从左到右画图,这二个函数都有一样的8个形参
- waveformGraph_y()函数,画波形图函数,沿Y轴垂直方向,从下到上画图,后7个参数间有一定互相关连影响,要试调确定
            turtle调用该函数的对象(实例)
            X 横坐标值
            Y 垂直坐标值
            adjustment整型参数,调整波形起点及完善图形对称,取值范围0-20(可取正、负数),默认值=0
            width整型参数,画波形图宽或长度值,偶数能被2整除(对称),取值范围一般不低于40,默认值=246
            amplitude整型参数,波形幅度值,该值越大波形幅度越大,取值范围4 - 100,默认值=10
            frequency整型参数,波形频率,该值越大波形越多,取值范围1 - 10,默认值=2
            coefficient整型参数,调整系数,该值越小波形越密越多,取值范围10 - 160,默认值=100

- drawRectangle()画方形图函数,5个形参:
            turtle调用该函数的对象(实例)
            width1整型参数,第一条边长
            height2整型参数,第二条边长
            coloring布尔变量参数,值是True时所绘图形,不充填颜色是False(黙认值)
            turn字符串参数,笔旋转方向,'left'向左(黙认值)转,'right'向右转

- fivePointedStar()创建画5角星函数,3个形参:
            turtle调用该函数的对象(实例)
            size整型参数,五角星对角线长度,2的整倍数
            coloring布尔变量参数,值是True时所绘图形,不充填颜色是False(黙认值)
"""
import turtle
import math  #导入python自带的数学函数库math

#定义多用途(可绘多种图型)绘画函数turtleStar(),有6个形参如上述
def turtleStar(turtle,length=100,corner=170,turn='left',coloring=False,stamp=False):
    x=round(turtle.xcor())   #round()是"四舍六入五成偶"舍入到小数点后n位精度的值的函数。本例无小数位参数则返回整数.保存画图开始的画笔坐标x值
    y=round(turtle.ycor())   #保存画图开始时的画笔坐标y值,以便下边循环画图到初始点时退出循环。xcor()和ycor()返回的是有14位小数的浮点数
    if coloring == True :   #如实参coloring值为真时就执行下边命令充填色.该值黙认为假,不充填,此参数在调用时如不充填色可省略.
        turtle.begin_fill()    #下边画图将充填颜色
    if stamp == True :      #当第5个参数是True时留下笔起点印章，此参数可省略，黙认False,不留
        turtle.stamp()       #绘画起始位留下画笔印章,以便观察和分析起点坐标

    while True:     #while循环绘直线条构成图形
        turtle.forward(length)   #画笔按它的朝向前进画length实参长度值直线条
        if turn == 'right' or turn == 'Right' :     #if判定turn是否向右转,只有传入'right'或'Right'才能右转
            turtle.right(corner)      #设置画笔向右转corner实参角度值
        else:                   #除上外,传入的其它字符均视为左转
            turtle.left(corner)      #设置画笔向左转corner实参角度值

        if round(turtle.xcor())== x and round(turtle.ycor())== y :    #循环画线退出条件:当画笔坐标值(x,y)与起点相等时即回到起点就退出循环
            if coloring == True :   #如实参coloring值为真时就执行下边命令充填色.该值黙认为假,不充填,此参数在调用时如不充填色可省略.
                turtle.end_fill()    #在begin_fill()之间的所有绘图填色完成

            break               #退出循环语句

# 定义无移动笔迹线函数noTraceGoto() 有4个形参:调用对象turtle
# 横坐标x值,垂直坐标y值,角度angle,黙认值均等于0
def noTraceGoto(turtle,x=0,y=0,angle=0):   #有三个形参分别是横坐标x值,垂直坐标y值,角度angle,黙认值均等于0
    turtle.pu()     # 抬起画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条,还可用penup(),up()
    turtle.goto(x,y)  # 移动海龟画笔到坐标x,y位置准备绘图,还可用setpos()
    turtle.setheading(angle)    #还可用seth(),将画笔朝向转到angle角度位,黙认值是标准模式时0,向屏幕右(东),
    turtle.pd()   # 放下画笔准备画图, 还可用pendown() ; down()

#定义根据画笔朝向和袳动步数来移动画笔不留笔迹线条函数,有5个形参
def move(turtle,angle1,step1,angle2=0,step2=0):
    turtle.pu() #抬起画笔,移动画笔不留笔迹线条
    turtle.seth(angle1) #将画笔朝向转到angle1角度位
    turtle.fd(step1) #向前移step1,负数为后退step1
    turtle.seth(angle2) #将画笔朝向转到angle2角度位
    turtle.fd(step2) #向前移step2,负数为后退step2
    turtle.pd() #放下画笔准备画图

#定义画椭园形函数turtleEllips()有5个形参
def turtleEllips(turtle,angle=3,initial=0.4,idquantity=0.08,radian=360):
    cycles = int(360/angle) #求出椭圆循环画线笔次数,与每次循环画线画笔转角度值相关,角度和应是360
    arc = int(cycles/4) #椭园的整个园弧从开画起点均分成4段,求出每段画的笔数值,int()
    arc2= arc*2 #第3段的起始笔数值
    arc3= arc*3 #第3段的结束笔数值
    if radian != 360 : #当不等于360度时即只画出椭圆一段弧形线
        cycles = int(radian/angle) #求出本次不是360度椭圆弧线画笔次数
    for i in range(cycles): #for循环画椭圆弧,从i=0开始,每循环1次i=i+1,到i=cycles时退出循环
        if 0<= i < arc or arc2 <= i < arc3: #画第1段或画第3段时,每次递增量
            initial = initial + idquantity #在此条件下每循环1次画线的长度递增变量delivery的值
            turtle.lt(angle) #画笔向左转变量angle的值角度
            turtle.fd(initial) #画笔按它的朝向前进变量initial的值画出直线条
        else: #画第2段或画第4段时,每次递减量
            initial = initial - idquantity #在此条件下每循环1次画线的长度递减变量delivery的值
            turtle.lt(angle) #画笔向左转变量angle的值角度
            turtle.fd(initial) #画笔按它的朝向前进变量initial的值画出直线条

#画波形图函数,沿X轴水平方向,从左到右画图,有8个形参,后三个参数是对波形调整,注意取值范围
def waveformGraph_x (turtle,x,y,width=246,adjustment=0,amplitude=10,frequency=2,coefficient=100):
    turtle.penup()
    turtle.goto(x,y) #开始画图坐标x,y起点
    turtle.setheading(0) #画笔指向角度0,朝右
    turtle.pendown()
    z=-width/2 #波形图宽度值的二分之一取负,是波形图最左边起点波形计算值,负正分二段后其图形左右才会是对称
    for i in range(x,width+x):#循环画波形,从起点x坐标开始,达波形宽度值结束,width+x是当x坐标不是原点0时,保证波形宽度值不变
              #y坐标就是波形计算值,函数math.cos()返回(z/coefficient)*frequency*math.pi弧度的余弦值,math.pi是常数圆周率
        turtle.goto(i,y+adjustment-amplitude*math.cos((z/coefficient)*frequency*math.pi))
        z=z+1 #每循环一次z变量增加1,代入上边计算公式参与计算并画波形线条中的一个点
    turtle.goto(turtle.xcor(),y) #让尾笔近似图出与起笔对称收尾线,xcor()获取现时画笔x坐标


#画波形图函数,沿Y轴重直方向,从下到上画图,有8个形参,后三个参数是对波形调整,注意取值范围
def waveformGraph_y (turtle,x,y,width=246,adjustment=0,amplitude=10,frequency=2,coefficient=100):
    turtle.penup()
    turtle.setheading(90) #画笔指向角度90,朝上
    turtle.goto(x,y) #开始画图坐标x,y起点
    turtle.pendown()
    z=-width/2 #波形图宽度值的二分之一取负,是波形图最下边起点波形计算值,负正分二段后其图形上下才会是对称
    for i in range(y,width+y):#循环画波形,从起点y坐标开始,达波形宽度值结束,width+y是当y坐标不是原点0时,保证波形宽度值不变
                #x坐标就是波形计算值,函数math.cos()返回(z/coefficient)*frequency*math.pi弧度的余弦值,math.pi是常数圆周率π = 3.141592...
      turtle.goto(x-adjustment+amplitude*math.cos((z/coefficient)*frequency*math.pi),i)
      z=z+1 #每循环一次z变量增加1,代入上边计算公式参与计算并画波形线条中的一个点
    turtle.goto(x,turtle.ycor()) #让尾笔近似图出与起笔对称收尾线,ycor()获取现时画笔y坐标

#创建画方形图函数,5个形参:第一条边长width1,第二条边长height2,是否填色coloring,画图方向turn
def drawRectangle(turtle,width1, height2,coloring=False,turn='left'):
    if coloring == True : #如coloring是True则开始准备填充颜色
        turtle.begin_fill()
    for i in range (2): #开始for循环2次画方形四个边
          turtle.forward(width1) #第一次循环画第一边第二次循环画第三边
          if turn == 'right' or turn == 'Right' : #如turn是'right',则画完一边画笔向右转90度
              turtle.right(90)
          else: #否则,则画完一边画笔向左转90度
              turtle.left(90)
          turtle.forward(height2) #第一次循环画第二边第二次循环画第四边
          if turn == 'right' or turn == 'Right' : #如turn是'right',则画完一边画笔向右转90度
              turtle.right(90)
          else: #否则,则画完一边画笔向左转90度
              turtle.left(90)
    if coloring == True : #如coloring是True则填充颜色完成
        turtle.end_fill()
    turtle.setheading(0) #画笔朝向回到初始方向,向屏幕右边

#创建画5角星函数,3个形参:size五角星对角线长度,2的整倍数.是否填色coloring,布尔变量
def fivePointedStar(turtle,size,coloring=False):
    x = size/2 #启笔是从五角星对角边中间开始画,故取size的二分之一
    if coloring == True : #如coloring是True则开始准备填充颜色
      turtle.begin_fill()
    turtle.right(144) #画笔从初始朝向右转144度
    for i in range(5): #for循环5次画五角星
          turtle.forward(x) #画x长直线
          turtle.right(144) #画笔向右转144度
          turtle.forward(x)
    if coloring == True : #如coloring是True则填充颜色完成
      turtle.end_fill()
    turtle.setheading(0) #画笔朝向回到初始方向,向屏幕右边

#运行本程序的自创函数简单演示部份,当本模块被其它程序导入时可自动识别而不会执行以下语句
if __name__ == "__main__":   # execute only if run as a script,模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行下边代码，而在被 import 时不会执行
        #调自定义函数绘图可修改下边各调用实参数观察变化
        turtle.colormode(255)    #设置窗口颜色RGB模式,1.0或255其中之一,255模式不兼容英语单词设置颜色
        turtle.bgcolor(29,162,216)   #设置显示窗口的背景颜色, 29,162,216是海兰色的RGB值,可从调色器advanced_colormixer.py上查看
        turtle.colormode(1.0)       #设置窗口颜色RGB模式,1.0或255其中之一. 1.0是系统默认设置,以便也可用英语单词设置颜色.
        turtle.speed(6)     # 画笔画图速度设置,速度关系按1,2,3,4,5,6,7,8,9,0排列,1最慢(初学时方便观察),最快是0.默认正常速度是6,可据自已要求修改
        turtle.color('red', 'yellow')  #设置对应海龟画笔的颜色和填充颜色
        noTraceGoto(turtle,50,100,0)   #移动海龟画笔到坐标x=50 ,y=100,画笔朝向0,朝屏幕右边 (东),回到初始状态
        turtleStar(turtle,280,170,'left',True,True)     #调自定义函数绘手册上的turtle star海龟星(角度值=170是海龟星特征角度)
        noTraceGoto(turtle,-150,-150,90)   #移动海龟画笔到坐标x=-150 ,y=-200,画笔朝向90,朝屏幕上边 (北)
        turtle.stamp()    #绘画起始位留下画笔印章,以便观察和分析起点坐标
        turtleEllips(turtle,2,0.3,0.1) #调自定义函数turtleEllips()画椭圆
        turtleEllips(turtle,2.5) #调自定义函数turtleEllips()画椭圆
        turtleEllips(turtle,3.2) #调自定义函数turtleEllips()画椭圆
        turtleEllips(turtle,3.4) #调自定义函数turtleEllips()画椭圆
        turtle.color("blue","green")  # 设置画笔颜色和填充颜色
        waveformGraph_x(turtle,50,-200,246,0,10,2,100) #画波形图函数,沿X轴水平方向,从左到右画波形图
        waveformGraph_x(turtle,50,-210,246,0,10,2,100)
        waveformGraph_y(turtle,-200,0,246,0,10,2,100) #画波形图函数,沿Y轴垂直方向,从下到上画波形图
        turtle.mainloop()  #调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句