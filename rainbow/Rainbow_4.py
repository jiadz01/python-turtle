"""绘画彩虹 Rainbow_4.py 可供其它程序导入,调用rainbow绘画彩虹函数,模块最后有一运行简单演示部份
本程序是在Rainbow_3.py的基础改变,直接画出赤-橙-黄-绿-青-蓝-紫彩虹色7条,各色条无颜色渐变

自定义2个函数:
- halfEllips()函数,可在turtle窗口任意坐标位置绘不同大小的半椭园形,有3个行参：
            initial浮点数参数,椭圆初始弧线数,取值范围0.1 - 8,黙认值0.4,值越大图形越大,也渐由椭园变成园形
            idquantity浮点数参数,每笔画线增減量,取值范围0.02 - 0.6,黙认值0.2,值越大椭圆越长越大
            angle浮点数参数,每画一次画笔向左转角度值,取值范围1.5 - 4,黙认值1.5,值越大椭圆小,值越小椭圆大
    initial和angle的值都越小,画出的椭圆越大也越椭(越长),所有参数都应在取值范围内！

- rainbow()函数,绘画彩虹,有8个形参:
    X 横坐标值
    Y 垂直坐标值
    size 画笔粗细尺寸(每画一次),默认值=10,可取值1,2,.....20
    initial浮点数参数,椭圆初始弧线数,取值范围0.1 - 8,黙认值1.0,值越大图形越大,也渐由椭园变成园形
    idquantity浮点数参数,每笔画线增減量,取值范围0.02 - 0.6,黙认值0.2,值越大椭圆越长越大
    angle浮点数参数,每画一次画笔向左转角度值,取值范围1.5 - 4,黙认值1.5,值越大椭圆小,值越小椭圆大
    axial 字符串变量,画彩虹时每画一次画笔移动轴向,默认值='y'(沿y轴减少), 可取值'x'(沿x轴减少)或'y'
    towards 画笔起始方向,默认值=90,可取值0-359,常用0,90,180,270
"""
import turtle   #导入turtle模块，调用其对象和函数等功能

#定义画半椭园形函数halfEllips()有3个形参如上述
def halfEllips(initial=1.0,idquantity=0.2,angle=1.5):
    cycles = int(180/angle) #求出半椭圆循环画线笔次数,与每次循环画线画笔转角度值相关,角度和应是180
    arc = int(cycles/2) #椭园的整个园弧从开画起点均分成2段,求出每段画的笔数值,int()
    arc2= arc*2 #第3段的起始笔数值
    arc3= arc*3 #第3段的结束笔数值
    for i in range(cycles): #for循环画椭圆弧,从i=0开始,每循环1次i=i+1,到i=cycles时退出循环
        if 0<= i < arc : #画第1段或画第3段时,每次递增量
            initial = initial + idquantity #在此条件下每循环1次画线的长度递增变量delivery的值
            turtle.lt(angle) #画笔向左转变量angle的值角度
            turtle.fd(initial) #画笔按它的朝向前进变量initial的值画出直线条
        else: #画第2段段时,每次递减量
            initial = initial - idquantity #在此条件下每循环1次画线的长度递减变量delivery的值
            turtle.lt(angle) #画笔向左转变量angle的值角度
            turtle.fd(initial) #画笔按它的朝向前进变量initial的值画出直线条
#绘制彩虹函数,带有8个形参
def rainbow(x,y,size=10,initial=1.0,idquantity=0.2,angle=1.5,axial='y',towards=90,):
    visible = turtle.isvisible() #测试原海龟笔是否可见,显示返回True,隐藏返回False,布尔变量
    turtle.speed(0) #画笔画图速度设置,1最慢,速度关系按1,2,3,4,5,6,7,8,9,0排列  最快是0
    turtle.hideturtle() #隐藏海龟画笔,ht()
    pensize = turtle.pensize()    #变量pensize保留当前海龟画笔粗细设置,    还可用还可用width()
    turtle.pensize(size) #画笔粗细尺寸设置
    turtle.penup() #抬起画笔
    turtle.goto(x,y) #画彩虹起始坐标位
    turtle.pendown() #放下画笔

    colors=[[1,0,0],[1,0.5,0],[1,1,0],[0,1,0],   #建立绘图所用变换的颜色列表,以便绘每条线时按列表下标取对应颜色值
        [0,1,1],[0,0,1],[1,0,1]]            #上边一行的续行,是一条命令行
    #colors=['red','orange','yellow','green','cyan','blue','purple']   #建立绘图所用变换的颜色列表,等效上条语句

    for i in range(7): #for循环,画实参变量width的值次数园,完成后退出循环（i=0....i=6)
        turtle.color(colors[i])  #设置画笔RGB值颜色
        turtle.seth(towards) #设置画笔朝向
        halfEllips(initial,idquantity,angle) #调画半椭园形函数画半椭园园
        turtle.penup() #抬起画笔
        if axial == 'x' or axial == 'X': #判定画彩虹时的轴向参数是否是'x'
            x=x-size #是,每画一个园x轴坐标就向左移动画笔粗细大小的坐标位
        else:
            y=y-size #否,每画一个园y轴坐标就向下移动画笔粗细大小的坐标位(默认设置)
        turtle.goto(x,y) #画下一个彩虹(园)坐标位
        turtle.pendown() #放下画笔
    turtle.pensize(pensize)    #画笔回到调用前粗细设置
    if visible == True : #画笔回到调用前是否显示或隐藏状态
        turtle.showturtle()  #显示海龟笔.还可用st()
        turtle.seth(towards) #画笔回到设置画笔朝向
    turtle.penup() #抬起画笔

#运行本程序的自创函数简单演示部份,当本模块被其它程序导入时可自动识别而不会执行以下语句
if __name__ == "__main__": # execute only if run as a script
    #调自定义绘制彩虹函数绘图,可修改下边各调用实参数观察绘图变化
    #turtle.tracer(False) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(0)等效
    rainbow(330,0,11) #调自定义绘制彩虹函数绘图,后边另5个参数选用默认值故可不填写实参数
    rainbow(360,-200,6,1.0,0.2,1.5,'x') #调自定义绘制彩虹函数绘图,后边另1个参数选用默认值故可不填写实参数
    #turtle.tracer(True) #恢复启用/禁用动画设置函数,还可用tracer(1)等效
    turtle.mainloop() #开始事件循环,调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句