#原python示范程序colormixer.py,其功能是显示RGB颜色模型的调色变化,窗口背景颜色就是这三原色各值的叠加结果.
#只用中文对每条语句注释
#将鼠标光标移到调色海龟上边，按住鼠标左键上下拖动海龟调值大小,只能关闭绘图窗口退出程序运行.
#改写升级版本详见color_1.py,color_2.py,color_rgb.py(比较这一系列程序可学习一些写程序技术)


from turtle import Screen, Turtle, mainloop     #从turtle库中导入选择Screen, Turtle, mainloop的对象或模块,
                                                #在本程序中直接调用,不需要指明调用函数的从属关系
#定义调色海龟笔 类 ColorTurtle()
class ColorTurtle(Turtle):  #创建调色海龟子类ColorTurtle,它继承的父类是Turtle,类名的首字母大写,如无继承而新建类则括号是空的
                            #根据类来创建对象(实例化),面向对象编程是最有效软件编写方法之一

    def __init__(self, x, y):   #类的专有方法__init__(),调用时自动传入调用实参self,只需对形参x,y给出实参(这里是画笔海龟的初始坐标)
        Turtle.__init__(self) #让父类Turtle的属性与子类ColorTurtle关联起来才能正常使用,如无继承而新建类则无此命令行
        self.shape("turtle")  #设置画笔海龟形状,可选:arrow,turtle,circle,square,triangle,classic改变形状,默认classic
        self.resizemode("user") #调整海龟大小模式,可选auto(根据笔粗细调整外观),user(拉伸因子和轮廓宽度调整),noresize
        self.shapesize(3,3,5) #设置海龟或笔的拉伸因子和轮廓宽度
        self.pensize(10)  # 海龟画笔绘图粗细尺寸设置,默认值 1最细
        self._color = [0,0,0]  #初始一个用于RGB颜色值全是零的列表,
        self.x = x      #将x的实参(海龟x坐标值)赋值给对应的变量self.x,供后边的shift()函数调用
        self._color[x] = y      #将RGB颜色值的列表中下标值为x的值修改成y实参值,本例主函数中调此类3次创建调色海龟实例:
                                #red调用时该值就修改成[0.5,0,0], green调用时该值就修改成[0,0.5,0], blue调用时该值就修改成[0,0,0.5]
        self.color(self._color) #用对应的RGB颜色值列表设置对应海龟画笔的颜色和填充颜色
        self.speed(0)   # 画笔画图速度设置0最快,默认速度是6,如果调慢可看到程序初期运行步骤
        self.left(90)   #设置画笔向左转90角度,这时画笔朝向屏幕上边,因初始化默认是朝屏幕右边方向
        self.pu()   # 抬起海龟画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条  还可用penup(); up()
        self.goto(x,0)  # 移动海龟画笔到坐标x,y=0位置   还可用setpos()
        self.pd()   # 放下画笔  还可用pendown() ; down()
        self.sety(1) #设置画笔海龟y坐标为1,横坐标不变,是从下到上画每个海龟下边的红 绿 兰三条竖线,每调用一次绘出一条
        self.pu()   # 抬起画笔,这样移动画笔过程中不留笔迹线条  还可用penup(); up()
        self.sety(y)    #设置画笔海龟移动到y坐标,x坐标不变
        self.pencolor("gray25")     # 设置海龟画笔颜色，海龟轮廓颜色,  颜色（gray)后边还可加数字1...100标示该色的调色变化
        self.ondrag(self.shift,btn=1)     # Using events 当鼠标拖动时将鼠标坐标x,y传入下边定义的与self.对应(绑定)的函数shift(), 本语句是亊件循环入口处
                                            # btn=1是设置拖动时按鼠标按钮编号1(鼠标左键),也是默认值

    def shift(self, x, y):  #当鼠标拖动时调用此函数,参数self和鼠标坐标x,y自动传入
        self.sety(max(0,min(y,1)))  #设置对应(绑定)的海龟画笔Y坐标,显示出像鼠标拖动它上下移动
                                        # max(0,min(y,1))算式是使移动值只能在0.0和1.0范围内,显示出超过这个范围鼠标就拖不动海龟画笔了
        self._color[self.x] = self.ycor()   #将RGB颜色值的列表中下标值为x的值修改成该海龟画笔的y坐标值
        self.fillcolor(self._color)     #设置对应海龟画笔充填颜色,本例主函数中调此类3次创建调色海龟实例:参数self=red,green,blue
        setbgcolor()    # 调用下边自已定义的函数设置显示窗口的背景颜色

#定义设置窗口背景颜色函数setbgcolor()
def setbgcolor():
    #由三个海龟画笔red.ycor(), green.ycor(), blue.ycor()的坐标y值正好组成背景颜色的RGB值,用此值改变背景颜色
    screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())

#程序主函数main()
def main():
    global screen, red, green, blue#设置screen, red, green, blue为全局变量,以便在其它调用函数和对象中传递数据
    screen = Screen()   #创建一个我们命名为screen的Screen实例，用来显示海龟调色的屏幕窗口
    screen.delay(0)   #对我们创建的窗口动画控制延迟设置,0是零毫秒,没有延迟 动画速度最快,如果设到300毫秒以上可看到程序初期运行步骤
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)  #设置世界坐标系,图像窗口左下角x,y坐标-1,-0.3 右上角x,y坐标3,1.3

    red = ColorTurtle(0, 0.5)   #以初始坐标x=0,y=0.5调用类ColorTurtle()创建一个红色调色海龟对象,参数self='red'
    green = ColorTurtle(1, 0.5) #以初始坐标x=1,y=0.5调用类ColorTurtle()创建一个绿色调色海龟对象,参数self='green'
    blue = ColorTurtle(2, 0.5)  #以初始坐标x=2,y=0.5调用类ColorTurtle()创建一个蓝色调色海龟对象,参数self='blue'
    setbgcolor()    #调用自已定义的函数设置窗口背景颜色

    writer = Turtle() #创建书写海龟笔writer对象实例,下边调用相关函数时均要加前(writer.)指明从属关系
    writer.ht() # 隐藏海龟画笔,写完字后不留笔的形态,画面干净.还可用hideturtle()
    writer.pu()  # 抬起画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条,还可用penup(),up()
    writer.goto(1,1.15) #到拟写字的坐标位置
    writer.write("DRAG!",align="center",font=("Arial",30,("bold","italic")))
    return "EVENTLOOP"

#程序实际执行起点
if __name__ == "__main__": # execute only if run as a script,模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行一些代码，而在被 import 时不会执行
    msg = main()    #从这里开始执行本程序命令,调用主函数main()
    print(msg)

    mainloop()  #开始事件循环,调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句