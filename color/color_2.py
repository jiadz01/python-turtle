''' color_2.py 其功能是显示RGB颜色模型的调色变化,窗口背景颜色就是这三原色各值的叠加结果.
1.由colo_1.py改写并对每条语句注释,变成turtle绘图调色实用工具(获取各种颜色的RGB值).
2.在绘画窗口顶部的标题栏中显示turtle三种RGB颜色模式的值,括号外是RGB 1.0模式的值,括号内是值RGB 255模式的值,
  前边带#的是16进制编码值.
3.使用方法: 将鼠标光标分别移到调色海龟上边，按住鼠标左键上下拖动海龟调颜色值大小,可见窗口背景颜色动态变化
           按键盘p键,在Python shell窗口或界面打印出所选颜色的RGB值(临时记录),
           按键盘Q键退出程序运行,并关闭绘画窗口.
注意:
1.本程序采用了自定义的世界坐标系,图像窗口左下角x,y坐标是-1,-0.3,右上角x,y坐标是3,1.3,与颜色值计算相匹配.
2.这是Python面向对象利用类(class)来编程的示范,根据类来创建对象(实例化),面向对象编程是最有效软件编写方法之一.
3.最终使用版本是color_rgb.py
'''
#from turtle import * #导入turtle模块,星号* 不需要指明调用函数的从属关系,直接按turtle定义的名称使用其对象和函数.
from turtle import Screen, Turtle, mainloop #从turtle库中导入Screen, Turtle, mainloop对象、类或模块
                                            #在本程序中直接调用,不需要指明调用函数的从属关系
#定义调色海龟笔 类 ColorTurtle()
class ColorTurtle(Turtle):  #创建调色海龟子类ColorTurtle,它继承的父类是Turtle,类名的首字母大写,
                            #如无继承而新建类则括号是空的
    def __init__(self, x, y):   #类的专有方法__init__(),调用时自动传入调用实参self,只需对形参x,y给出实参
                                #这里x,y是画笔海龟的初始坐标.
        Turtle.__init__(self) #让父类Turtle的属性与子类ColorTurtle关联才能使用,如无继承而新建类则无此命令行.
        self.shape("turtle")  #设置画笔海龟形状,可选:arrow,turtle,circle,square,triangle,classic改变形状.
        self.resizemode("user") #调整海龟大小模式,可选auto(根据笔粗细调整外观),user(拉伸因子和轮廓宽度调整)等.
        self.shapesize(3,3,5) #设置海龟或笔的拉伸因子和轮廓宽度
        self.pensize(10)  #海龟画笔绘图粗细尺寸设置,默认值 1最细
        self._color = [0,0,0]  #初始一个用于RGB颜色值全是零的列表,
        self.x = x      #将x的实参(海龟x坐标值)赋值给对应的变量self.x,供后边的shift()函数调用
        self._color[x] = y #将RGB颜色值的列表中下标值为x的值修改成y实参值,本例主函数中调此类3次创建调色海龟
            #实例: red调用时该值[0.5,0,0],green调用时该值就改成[0,0.5,0],blue调用时该值就修改成[0,0,0.5]
        self.color(self._color) #用对应的RGB颜色值列表设置对应海龟画笔的颜色和填充颜色
        self.speed(0)   # 画笔画图速度设置0最快,默认速度是6,如果调慢可看到程序初期运行步骤
        self.left(90)   #设置画笔向左转90角度,这时画笔朝向屏幕上边,因初始化默认是朝屏幕右边方向
        self.pu()   # 抬起海龟画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条,还可用penup(); up()
        self.goto(x,0)  # 移动海龟画笔到坐标x,y=0位置   还可用setpos()
        self.pd()   # 放下画笔  还可用pendown() ; down()
        self.sety(1) #设置画笔海龟y坐标为1,横坐标不变,是从下到上画每个海龟下边的红 绿 兰三条竖线,调一次绘出一条
        self.pu()   # 抬起画笔,这样移动画笔过程中不留笔迹线条  还可用penup(); up()
        self.sety(y)    #设置画笔海龟移动到y坐标,x坐标不变
        self.pencolor("gray25") #设置海龟画笔颜色,海龟轮廓颜色
        self.ondrag(self.shift,btn=1) # Using events 当鼠标拖动时将鼠标坐标x,y传入下边定义的与self.对应
                                    #(绑定)的改变背景颜色方法shift(), 本语句是亊件循环入口处,
                                    # btn=1是设置拖动时按鼠标按钮编号1(鼠标左键),也是默认值.
    #定义当鼠标拖动调色海龟(对象)改变背景颜色方法shift()
    def shift(self, x, y):  #当鼠标拖动时调用此函数,参数self和鼠标坐标x,y自动传入
        self.sety(max(0,min(y,1)))  #设置对应(绑定)的海龟画笔Y坐标,显示出像鼠标拖动它上下移动
                # max(0,min(y,1))算式是使移动值只能在0.0和1.0范围内,显示出超过这个范围鼠标就拖不动海龟画笔了
        self._color[self.x] = self.ycor() #将RGB颜色值的列表中下标值为x的值修改成该海龟画笔的y坐标值
        self.fillcolor(self._color) #设置对应海龟画笔充填颜色,本例主函数中调此类3次创建调色海龟实例:
                                    #参数self=red,green,blue
        setbgcolor()    # 调用下边自已定义的背景颜色函数,设置显示窗口的背景颜色

#定义设置窗口背景颜色函数setbgcolor()
def setbgcolor():
    global rgb_255,rgb_1,rgb_16#设置为全局变量,以便在调用临时记录函数中传递数据
    #由三个海龟画笔red.ycor(), green.ycor(), blue.ycor()的坐标y值正好组成背景颜色的RGB值,改变背景颜色
    screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())
    #rgb_1生成RGB模式1.0字符串,format()格式函数保留小数点后2位
    rgb_1=str(format(red.ycor(),'0.2f'))+' , '+str(format(green.ycor(),'0.2f'))+' , '+ \
            str(format(blue.ycor(),'0.2f')) #两个及两个以上的物理行可用反斜杠（\）拼接为一个逻辑行
    #rgb_255生成RGB模式255字符串,ycor()是在0.000和1.000之间的数,乘255后取整数位数转换成该模式对应值
    rgb_255=str(int(red.ycor()*255))+' , '+str(int(green.ycor()*255))+' , '+str(int(blue.ycor()*255))
    #rgb_16生成RGB模式16进制码字符串,由RGB255模式转换成16进制颜色码
    #rgb_16='%X%X%X' %(int(red.ycor()*255),int(green.ycor()*255),int(blue.ycor()*255))
    #上下二条语句等效,只需其中一条,另一条应#注释掉
    rgb_16='{:X}{:X}{:X}'.format(int(red.ycor()*255),int(green.ycor()*255),int(blue.ycor()*255))
    #十六进制色码是每个单色是两位编码,故当值低于16时应在个位前加'0'占位,由下边3个if语句完成
    #python中字符串为不可变类型,只能以新建方式新增修改,下边用切片方式增加并重建字符串
    if int(red.ycor()*255) <= 15:
        rgb_16='0'+rgb_16
    if int(green.ycor()*255) <= 15:
        rgb_16=rgb_16[:2]+'0'+rgb_16[2:]
    if int(blue.ycor()*255) <= 15:
        rgb_16=rgb_16[:4]+'0'+rgb_16[4:]
    rgb_16='#'+rgb_16
    #将3个颜色模式值显示在绘画窗口最上的标题内容
    screen.title('Color mode RGB value:    '+rgb_1+'    ( '+rgb_255+' )'+'    Hexadecimal code: '+rgb_16)

#定义临时记录函数
def records(): #在Python shell窗口或界面打印出所选颜色的RGB值(临时记录)
    global rgb_255,rgb_1,rgb_16 #设置为全局变量,以便在调用函数中传递数据
    print('RGB Temporary records ------------')
    print('255 Mode: '+rgb_255)
    print('1.0 Mode: '+rgb_1)
    print('Hexadecimal code: '+rgb_16)

#程序主函数main()
def main():
    global screen, red, green, blue, writer,rgb_255,rgb_1 #设置为全局变量,以便调用函数和对象中传递数据
    screen = Screen()   #创建一个我们命名为screen的Screen实例，用来显示海龟调色的屏幕窗口
    screen.delay(0)   #对我们创建的窗口动画控制延迟设置,0是零毫秒,没有延迟,动画速度最快,
                      #如果设到300毫秒以上可看到程序初期运行步骤,可试看
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)  #设置世界坐标系,图像窗口左下角x,y坐标是-1,-0.3
                                                  #右上角x,y坐标是3,1.3
    screen.colormode(1.0)   #对我们创建的窗口设置颜色RGB模式,1.0或255其中之一，本列选1.0,也是系统默认设置

    writer = Turtle()   #创建书写海龟笔writer对象实例,下边调用相关函数时均要加前(writer.)指明从属关系
    writer.ht()     # 隐藏海龟画笔,写完字后不留笔的形态,画面干净.还可用hideturtle()
    writer.pencolor("gray35")     # 设置海龟画笔颜色
    writer.pu()     #抬起画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条,还可用penup(),up()
    writer.goto(1,1.15) #到拟写字的坐标位置
    title1="  Drag the turtle up and down with the mouse and press the left mouse button, "
    title2="and the background color is the color after the three colors are superimposed."
    title3=title1+"\n"+title2 #\n字符串中换行符
    writer.write(title3,align="center",font=("Arial",14,("bold","italic"))) #写出字符串,其它参数见文档
    for i in range(0,3):      #用for循环3次,i的值每次分别是0,1,2. 写出三条标线刻度的最大值
        writer.goto(i,1.03) #所写的坐标分别是:x=0 y=1.03,x=1 y=1.03,x=2 y=1.03
        writer.write("1.0 ( 255 )",align="center",font=("Arial",16,("bold","italic")))

    for i in range(0,3):      #用for循环3次,i的值每次分别是0,1,2. 写出三条标线刻度的最小值
        writer.goto(i,-0.09) #所写的坐标分别是:x=0 y=-0.09,x=1 y=-0.09,x=2 y=-0.09
        if i == 0:
            a = 'Red'
        elif i == 1:
            a = 'Green'
        else:
            a = 'Blue'
        writer.write("%s 0.0 ( 0 )" %(a),align="center",font=("Arial",16,("bold","italic")))
        #下边语句等效上条语句,字符串格式化操作的另一种写法
        #writer.write("{} 0.0 ( 0 )".format(a),align="center",font=("Arial",16,("bold","italic")))

    writer.goto(1,-0.25)     #写最下边的说明的中心坐标位置x=1 y=-0.25
    title1="Outside the brackets is the color RGB 1.0 mode"
    title2="The color RGB 255 mode in brackets"
    title3=title1+"\n         "+title2 #\n字符串中换行符
    writer.write(title3,align="center",font=("Arial",16,("bold","italic")))
    writer.goto(1,-0.3)
    writer.write("To exit press q or Q key",align="center",font=("Arial",12,("bold","italic")))

    red = ColorTurtle(0, 0.5)   #以初始坐标x=0,y=0.5调用自定义的类创建一个红色调色海龟对象,参数self='red'
    green = ColorTurtle(1, 0.5) #以初始坐标x=1,y=0.5调用自定义的类创建一个绿色调色海龟对象,参数self='green'
    blue = ColorTurtle(2, 0.5)  #以初始坐标x=2,y=0.5调用自定义的类创建一个蓝色调色海龟对象,参数self='blue'
    setbgcolor()    #调用自已定义的窗口背景颜色函数初始化窗口背景颜色
    screen.listen() #设置焦点接受按键亊件,下边是事件驱动(event-driven)语句
    screen.onkeypress(screen.bye,"q") #按键盘q键调用Screen()的专有方法bye(),退出程序运行
    screen.onkeypress(screen.bye,"Q") #按键盘Q键调用Screen()的专有方法bye(),退出程序运行
    screen.onkeypress(records,"p") #按键盘p键调用自已定义的records()临时记录函数

    return "color_RGB: main() END    EVENTLOOP"

#程序实际执行起点
if __name__ == "__main__":   # execute only if run as a script
    msg = main()    #从这里开始执行本程序命令,调用程序主函数main()
    print(msg) #在Python shell窗口或界面打印
    mainloop()  #调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句