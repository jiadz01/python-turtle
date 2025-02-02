""" Doraemon_paint.py是在adaptaion_paint.py的基础上扩展,增加导入画图函数来进行亊件驱动绘哆啦猫脸图 2021.4.5
学习并体会(A simple  event-driven paint program 亊件驱动程序)编程技巧和对导入函数补充调整以让它适应本程序的需求方法
本程序要导入自建的selfTurtleModule.py和Doraemon.py模块,它们应与本程序同在一个文件目录内.

使用方法：
- 移动鼠标按左键,画笔袳动到鼠标坐标位置  left mouse button moves turtle
        (在窗口标题栏中自动显示出当前画笔坐标值)
- 按鼠标右键或按键盘空格键,改变画笔颜色  right mouse button changes color
- 按键盘P键,第一次是画笔落下(移动画笔可画出线条图形)并将充填色同时显示标识,第二次按键是所画图形充填颜色并抬笔
- 按键盘Down键,落下画笔,移动画笔可画出线条图形,在绘图窗口左下角显示画笔落下标志(小箭头向下)
- 按键盘Up键,抬起画笔
- 按键盘F键,第一次是将充填颜色和显示充填标记(小正方形),第二次按键是充填完成和隐藏充填标志
- 按键盘D键,在画笔坐标位快速绘画哆啦猫脸
- 按键盘C键,清除屏幕画图,重新作画
- 按键盘Z键,窗口画出海龟标准坐标
- 按键盘Q键,退出程序运行  To exit press Q key
"""
import turtle as p   #创建一个turtle对象实例p, 调用turtle的函数或对象的名称前加(p.)
from selfTurtleModule import coordinate  #从selfTurtleModule.py模块中导入画海龟坐标图函数coordinate()
from Doraemon import doraemon #从Doraemon.py导入绘画哆啦猫脸函数doraemon()

label = p.Turtle() #创建一个Turtle类对象label用来标记画笔落下(屏幕左下角显示小箭头向下)或抬起(无显示)
fill = p.Turtle() #创建一个Turtle类对象fill用来标记画图充填色(屏幕左下角显示正四方形)或无充填(无显示)


def mydoraemon(x=0,y=0): #创建调整导入doraemon()的函数,以便能让doraemon适应在本模块中的应用
 #保留调用daraemon函数前海龟画笔的各原始状态和参数(调整内容)
    pcolor = p.pencolor()   #变量pcolor保留当前海龟画笔颜色,值是字符串或元组类
    tracer0 = p.tracer()    #保留启用/禁用动画并设置刷新延迟时间函数tracer()原值,这命令对画图速度影响很大
    if p.filling(): #防止在其它模块调用此函数时begin_fill()语句干扰,如有启用则将其终止
        p.end_fill()
        fill.ht()  #隐藏充填标志,还可用函数hideturtle()
    myUp() #调用自创函数,抬起画笔,隐藏画笔落下标志
    p.tracer(0) #启用/禁用动画并设置刷新延迟时间为0,这对画图速度很快,可前加#注释不执行,画得慢而便于观察
    p.shape("classic") #设置海龟画笔形状
    x=p.xcor() #取当前画笔x坐标值
    y=p.ycor() #取当前画笔y坐标值
    #从Doraemon.py导入绘画哆啦猫脸函数
    doraemon(x,y) #调用导入doraemon()函数,在x,y坐标绘画哆啦猫脸
    #让画笔回到调用doraemon函数前的各原始状态和参数(调整内容)
    p.tracer(tracer0)   #恢复启用/禁用动画设置函数tracer()原值
    p.pu()     # 抬起画笔
    p.shape("circle") #设置海龟画笔形状
    p.resizemode("user") #海龟大小调整模式
    p.shapesize(.5) #海龟形状大小
    p.width(3) #画笔回到调用前设置的粗细
    p.color(pcolor) #画笔回到调用前设置画笔颜色

def labelGoto(): #创建函数,定位画笔落下的标记在绘图窗口左下角的坐标
    label.goto(-int(p.window_width()/2)+17,-int(p.window_height()/2)+10)

def fillGoto(): #创建函数,定位画图充填颜色的标记在绘图窗口左下角的坐标
    fill.goto(-int(p.window_width()/2)+52,-int(p.window_height()/2)+26)

def penGoto(x=0,y=0): #创建函数,按鼠标键事件驱动的函数，将画笔移动到鼠标位置x,y的坐标
    p.goto(x,y) #画笔移动到实参x,y坐标位置
    x=round(p.xcor())   #round()是"四舍六入五成偶"舍入到小数点后n位精度的值的函数。本例无小数位参数则返回整数.保存画笔坐标x值
    y=round(p.ycor())   #保存画笔坐标y值。xcor()和ycor()返回的是有14位小数的浮点数
    p.title('This point coordinate:   X= '+str(x)+'   Y= '+str(y)+' \t      ( Pay attention to the sign of the number )\
        Click the right mouse button to change the color.\
        Click the C key to clear the screen.')  #画笔坐标x,y值也将显示在绘画窗口最上的标题栏

def switchupdown(x=0,y=0): #创建事件驱动的函数,此处有形参是便于用于鼠标事件驱动，它有坐标参数自动传入。
    if p.pen()["pendown"]: #如画笔已落下，操作是抬起画笔、充填完成并将它们对应的标志显示隐藏
        p.end_fill() #在begin_fill()之间的所有绘图填色
        p.up() # 抬起画笔,防止移动画笔时留下笔迹线条  还可用penup() ; pu()
        fill.ht() #隐藏充填标志,还可用函数hideturtle()
        label.ht() #隐藏画笔落下标志,还可用函数hideturtle()
    else:  #否则是落下画笔，准备充填颜色并显示对应的标志符号
        p.down() # 放下画笔  还可用pd() ; down()
        labelGoto() #定位画笔落下的标记在绘图窗口左下角的坐标位置
        label.st() #显示画笔落下的标记,还可用函数showturtle()
        p.begin_fill() #下边画图将充填颜色
        fillGoto() #定位画图充填颜色的标记在绘图窗口左下角的坐标位置
        fill.st() #显示画图充填颜色的标记,还可用函数showturtle()

def myDown(): #创建键盘事件驱动的函数,落下画笔,在绘图窗口左下角显示画笔落下标志
    p.down() # 放下画笔  还可用pd() ; down()
    labelGoto() #定位画笔落下的标记在绘图窗口左下角的坐标位置
    label.st() #显示画笔落下的标记,还可用函数showturtle()

def myUp(): #创建键盘事件驱动的函数,抬起画笔
    p.up() # 抬起画笔,防止移动画笔时留下笔迹线条  还可用penup() ; pu()
    label.ht() #隐藏画笔落下标志,还可用函数hideturtle()
    myfill() #利用函数myfill()对充填标志的一致性调整

def myfill(): #创建键盘事件驱动的函数,充填颜色操作
    if p.filling(): #如已开始充填就完成充填并隐藏充填标志显示
        p.end_fill() #在begin_fill()之间的所有绘图填色
        fill.ht()  #隐藏充填标志,还可用函数hideturtle()
    elif p.isdown():#如笔已落下则充填开始并在绘图窗口左下角显示充填标志
        p.begin_fill() #下边画图将充填颜色
        fillGoto() #定位画图充填颜色的标记在绘图窗口左下角的坐标位置
        fill.st() #显示画图充填颜色的标记,还可用函数showturtle()
        p.title('After drawing the picture, press the F key again to fill the picture with color.')  #将显示在绘画窗口最上的标题内容

def myCoordinate(): #创建键盘事件驱动的函数,画海龟坐标图,对原坐标函数适当补充以适应本模块
    coordinate() #从selfTurtleModule.py模块中导入画海龟坐标函数
    p.up() # 抬起画笔,防止移动画笔时留下笔迹线条  还可用penup() ; up()
    fill.ht()  #隐藏充填标志,还可用函数hideturtle()
    label.ht() #隐藏画笔落下标志,还可用函数hideturtle()

def changeColor(x=0, y=0): #创建事件驱动的函数,改变画笔、画笔落下标志和充填标志的颜色值
    global colors #全局变量colors,绘图所用变换的颜色值列表
    colors = colors[1:]+colors[:1] #利用列表切片方法，每执行一次组成一个新列表:列表最前一个值排到新列表最后
    p.color(colors[0]) #取列表最前一个值设置画笔颜色
    label.color(colors[0]) #取列表最前一个值设置画笔落下标志颜色
    fill.color(colors[0]) #取列表最前一个值设置充填标志颜色

def paint(): #创建本模块画板函数
    global colors #全局变量colors,绘图所用变换的颜色值列表
    colors=["pink","red","orchid4","green","red3","blue","orange","green3","royalblue1","yellow"] #建立绘图所用变换的颜色列表,以便绘图时按列表下标取对应颜色值
    changeColor() #用changeColor()函数初始设置画笔、画笔落下标志和充填标志的颜色
    p.shape("circle") #设置海龟画笔形状
    p.resizemode("user") #海龟大小调整模式
    p.shapesize(.5) #海龟形状大小
    p.width(3) #画笔粗细,还可用pensize()

    label.shape("classic") #设置标记画笔落下的海龟画笔形状
    label.resizemode("auto") #海龟大小调整模式
    label.up() # 抬起画笔,防止移动画笔时留下笔迹线条  还可用penup() ; pu()
    labelGoto() #定位画笔落下的标记在绘图窗口左下角的坐标
    label.shapesize(3) #海龟形状大小
    label.width(3) #画笔粗细,还可用pensize()
    label.right(90)  #向右转90度让三角形的尖角正对下方,因初始黙认是正对右边

    fill.shape("square") #设置标记充填颜色的海龟画笔形状
    fill.up() # 抬起画笔,防止移动画笔时留下笔迹线条  还可用penup() ; pu()
    fillGoto() #定位画图充填颜色的标记在绘图窗口左下角的坐标
    fill.shapesize(1) #海龟形状大小
    fill.width(2) #画笔粗细,还可用pensize()

    p.title('Click the left mouse button to move the pen. \
        Click the Down key to draw a line while moving the pen. \
        Click the F key to fill the drawing with color.\
        Click the Z key to draw the turtle coordinates.')  #将显示在绘画窗口最上的标题内容

    switchupdown() #用函数switchupdown()来初始化画笔抬起和使二个标志海龟隐藏
    p.listen() #设置焦点接受按键亊件,下边是事件驱动(event-driven)语句

    p.onscreenclick(penGoto,1) #按鼠标左键将鼠标坐标x,y 传入调用penGoto()函数,将画笔移动到鼠标位置x,y的坐标
    p.onscreenclick(changeColor,3) #按鼠标右键调用changeColor()函数改变画笔颜色
    #p.onscreenclick(mydoraemon,2) #用于配三键鼠标的第二键事件驱动,调用mydoraemon函数绘画哆啦猫脸,除去句首注释#符即可用
    p.onkeypress(changeColor,"space") #按键盘空格键调用changeColor()函数改变画笔颜色
    p.onkeypress(switchupdown,"p") #按键盘P键调用switchupdown()函数,第一次是落笔并将充填色,第二次按键是充填完成并抬笔
    p.onkeypress(myCoordinate,"z") #按键盘Z键调用myCoordinate()函数,窗口画出海龟标准坐标
    p.onkeypress(myDown,"Down") #按键盘Down键调用myDown()函数,落下画笔
    p.onkeypress(myUp,"Up") #按键盘Up键调用myUp()函数,抬起画笔
    p.onkeypress(myfill,"f") #按键盘F键调用myfill()函数,第一次是将充填色和显示充填标记,第二次按键是充填完成和隐藏充填标志
    p.onkeypress(mydoraemon,"d") #按键盘D键调用mydoraemon函数绘画哆啦猫脸
    p.onkeypress(p.clear,"c") #按键盘C键调用clear()函数,清除屏幕画图,重新作画
    p.onkeypress(p.bye,"q") #按键盘Q键调用bye()函数,退出程序运行
    return "Paint-EVENTLOOP"
#程序实际执行起点
if __name__ == "__main__":  # execute only if run as a script,模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行一些代码，而在被 import 时不会执行
    msg = paint() #从这里开始执行本程序命令,调用函数pain()
    print(msg)
    p.mainloop() #开始事件循环,调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句