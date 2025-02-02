"""绘画彩虹 Rainbow_5.py 可供其它程序导入,调用rainbow绘画彩虹函数,模块最后有一运行简单演示部份
本程序是在Rainbow_2.py的基础改变,直接画出赤-橙-黄-绿-青-蓝-紫彩虹色7条,各色条无颜色渐变
自定义1个函数:
- rainbow()函数,绘画彩虹,有7个形参:
    X 横坐标值
    Y 垂直坐标值
    size 画笔粗细尺寸(每画一次),默认值=1,可取值1,2,3
    radius 整数参数,彩虹圆弧半径,默认值=100,可取值30-500
    axial 字符串变量,画彩虹时每画一次画笔移动轴向,默认值='y'(沿y轴减少), 可取值'x'(沿x轴减少)或'y'
    extent 彩虹弧长的园弧夹角,默认值=180,可取值45-360
    towards 画笔起始方向,默认值=90,可取值0-359,常用0,90,180,270
"""
import turtle   #导入turtle模块，调用其对象和函数等功能

#绘制彩虹函数,带有8个形参
def rainbow(x,y,size=8,radius=100,axial='y',extent=180,towards=90):
    visible = turtle.isvisible() #测试原海龟笔是否可见,显示返回True,隐藏返回False,布尔变量
    turtle.speed(6) #画笔画图速度设置,1最慢,速度关系按1,2,3,4,5,6,7,8,9,0排列  最快是0
    turtle.hideturtle() #隐藏海龟画笔,ht()
    pensize = turtle.pensize()    #变量pensize保留当前海龟画笔粗细设置,    还可用还可用width()
    turtle.pensize(size) #画笔粗细尺寸设置
    turtle.penup() #抬起画笔
    turtle.goto(x,y) #画彩虹起始坐标位
    turtle.pendown() #放下画笔

    colors=[[1,0,0],[1,0.5,0],[1,1,0],[0,1,0],   #建立绘图所用变换的颜色列表,以便绘每条线时按列表下标取对应颜色值
        [0,1,1],[0,0,1],[1,0,1]]            #上边一行的续行,是一条命令行
    #colors=['red','orange','yellow','green','cyan','blue','purple']   #建立绘图所用变换的颜色列表,等效上条语句

    for i in range (7): #for循环,画实参变量width的值次数园,完成后退出循环（i=0....i=6)
        turtle.color(colors[i])  #设置画笔RGB值颜色
        turtle.seth(towards) #设置画笔朝向
        turtle.circle(radius,extent)  #调画园函数画园,圆的半径radius,园弧夹角extent
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
    rainbow(300,0,10,300) #调自定义绘制彩虹函数绘图,后边另3个参数选用默认值故可不填写实参数
    turtle.tracer(False) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(0)等效
    rainbow(300,-200,8,200,'x') #调自定义绘制彩虹函数绘图,后边另2个参数选用默认值故可不填写实参数
    turtle.tracer(True) #恢复启用/禁用动画设置函数,还可用tracer(1)等效
    turtle.mainloop() #开始事件循环,调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句