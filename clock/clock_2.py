'''clock_2.py 时钟 是clock_1.py的修改版本
1.在main()增加事件驱动,任何时候按键盘Q键,程序可终止运行而退出.
2.指针形态调整和改变背景颜色.
时间指针转动算法:创建3个海龟,让它分别使用自绘画并注册在海龟形状列表中的3个指针形状(时针分针秒针),
    用定时器函数ontimer()以递归(函数调用自身)方式,
    不间断地读取计算机系统时间日期和根据时间来调整海龟指针的朝向,让3根指针分别按时、分、秒转动.
'''
import turtle #导入turtle模块，调用其对象和函数等功能
import datetime #导入datetime模块，调用其创建对象、读取属性和方法等处理日期时间功能

#定义跳跃函数jump()  2形参,跳跃长度disranz,画笔转向度数winkel 默认值=0
def jump(distanz, winkel=0):
    turtle.penup() #抬起画笔,不留笔迹线条
    turtle.right(winkel) #画笔右转winkel,还可用rt()
    turtle.forward(distanz) #画笔前进distanz,还可用fd()
    turtle.left(winkel) #画笔左转winkel,还可用lt()
    turtle.pendown() #放下画笔,拟画线

#定义画指针函数hand()  3形参,指针长laenge,指针头三角形边长spitze,指针宽width
def hand(laenge, spitze, width=0):
    turtle.rt(90) #画笔右转90,还可用right()
    turtle.fd(width/2.0) #画笔前进画线width/2.0
    turtle.lt(90) #画笔左转90,还可用left()
    turtle.fd(laenge*1.15) #画笔前进画线laenge*1.15,还可用forward()
    turtle.rt(90) #画笔右转90,还可用right()
    turtle.fd((spitze-width)/2.0) #画笔前进画线(spitze-width)/2.0
    turtle.lt(120) #画笔左转120,还可用left()
    turtle.fd(spitze) #画笔前进画线spitze
    turtle.lt(120) #画笔左转120
    turtle.fd(spitze) #画笔前进画线spitze
    turtle.lt(120) #画笔左转120
    turtle.fd((spitze-width)/2.0) #画笔前进画线(spitze-width)/2.0
    turtle.rt(90) #画笔右转90,还可用right()
    turtle.fd(laenge*1.15) #画笔前进画线laenge*1.15,还可用forward()
    turtle.lt(90) #画笔左转90,还可用left()
    #turtle.fd(width/2.0) #画笔前进画线width/2.0

#定义注册指针形状函数,将一个海龟形状加入TurtleScreen的形状列表,4个形参,name为字符串变量,多边形的调用名称
def make_hand_shape(name, laenge, spitze, width=0): #指针长laenge,指针头三角形边长spitze,指针宽width
    turtle.reset() #重置,删除海龟绘图,海龟回原点(x=0,y=0),设置变量为默认值
    jump(-laenge*0.15) #海龟后退laenge*0.15,为画出指针定起点位置
    turtle.begin_poly() #开始记录海龟画图第一个顶点(起点)
    hand(laenge, spitze, width) #调自定义画时钟指针函数hand()画指针
    turtle.end_poly() #停止记录海龟画图,最后一个多边形项点,将与笫一个顶点连线
    hand_form = turtle.get_poly() #返回最新记录的多边形,赋予变量hand_form
    turtle.register_shape(name, hand_form) #添加形状,name为字符串变量是hand_form多边形的调用名称
        #还可用addshape(),只有这样注册后的形状才可被turtle.shape()调用

#定义画时针界面(秒和分钟刻度)函数clockface(),1个形参,radius时钟面半径
def clockface(radius):
    turtle.reset() #重置,删除海龟绘图,海龟回原点(x=0,y=0),设置变量为默认值
    turtle.pensize(7) #设置画笔粗细尺寸为7
    for i in range(60): #fo循环,i=0.....i=59,循环60次
        jump(radius) #调自定义跳跃函数jump(),到钟面半径radius处
        if i % 5 == 0: #i数除以5,取模求出余数,如无余数则能被5整除,画5分钟(秒)粗刻度
            turtle.fd(25) #画笔前进25画线
            jump(-radius-25) #调自定义跳跃函数jump(),画笔后退到原点
        else: #否则画1分钟(秒)园点刻度
            turtle.dot(3) #画直径为3园点
            jump(-radius) #调自定义跳跃函数jump(),画笔后退到原点
        turtle.rt(6) #画笔右转6度
    #在绘画窗口最上的标题栏中显示如下字符串
    turtle.title('Clock    ***    Press the keyboard Q key to exit the clock demonstration.')


#定义时钟各指针及书写画笔初始设置函数setup()
def setup():
    global second_hand, minute_hand, hour_hand, writer #设置为全局变量
    turtle.mode("logo") #设置海龟模式,有三种模式,standard海龟初始朝右,正数角度是逆时方向转
                        #logo模式海龟初始朝上,正数角度是顺时方向转.  world是用户自定义世界坐标系
    make_hand_shape("second_hand", 145, 15) #调定义注册指针形状函数,加入秒针形状,调用名称second_hand
    make_hand_shape("minute_hand",  130, 25, 6) #调定义注册指针形状函数,加入分针形状,调用名称minute_hand
    make_hand_shape("hour_hand", 90, 25, 6) #调定义注册指针形状函数,加入时针形状,调用名称hour_hand
    clockface(160) #调定义画时针界面函数,画秒、分和时刻度
    minute_hand = turtle.Turtle() #创建1个海龟对象实例,下边调用相关函数时均要加前minute_hand.指明从属关系
    minute_hand.shape("minute_hand") #设置这个海龟形状,前边注册分针形状,调用名称minute_hand(字符串)
    minute_hand.color("blue1", "red1") #设置这个海龟颜色blue1和充填颜色red1
    hour_hand = turtle.Turtle() #创建1个海龟对象实例,下边调用相关函数时均要加前hour_hand.指明从属关系
    hour_hand.shape("hour_hand") #设置这个海龟形状,前边注册时针形状,调用名称hour_hand(字符串)
    hour_hand.color("blue3", "red3") #设置这个海龟颜色blue3和充填颜色red3
    second_hand = turtle.Turtle() #创建1个海龟对象实例,下边调用相关函数时均要加前second_hand.指明从属关系
    second_hand.shape("second_hand") #设置这个海龟形状,前边注册秒针形状,调用名称second_hand(字符串)
    second_hand.color("gray20", "gray80") #设置这个海龟颜色gray20和充填颜色gray80
    for hand in second_hand, minute_hand, hour_hand: #利用for循环对这三个海龟对象进行如下设置
        hand.resizemode("user") #海龟大小调整模式user,auto,noresize，只有user模式下条语句才有效
        hand.shapesize(1, 1, 2) #基于拉伸因子调整海龟外观,垂直于朝向拉伸因子=1,平行于朝向拉伸因子=1
        hand.speed(0) #海龟画笔画图速度设置
    #在指针顶端加一个不动的指针帽
    cap = turtle.Turtle() #创建1个海龟对象实例,下边调用相关函数时均要加cap.指明从属关系
    cap.speed(0)
    cap.color("blue3", "red3") #设置这个海龟颜色blue3和充填颜色red3
    cap.shape("circle") #设置这个海龟形状为园形
    cap.shapesize(0.5, 0.5, 1) #基于拉伸因子调整海龟外观,垂直于朝向拉伸因子=0.5,平行于朝向拉伸因子=0.5

    turtle.ht() #隐藏海龟
    #创建一个专写星期几和日期的海龟画笔
    writer = turtle.Turtle() #创建1个海龟对象实例,下边调用相关函数时均要加前writer.指明从属关系
    #writer.mode("logo") #设置海龟模式
    writer.ht() #隐藏海龟,还可用hideturtle()
    writer.pu() #抬起画笔海龟,还可用up(),penup()
    writer.bk(85) #后退85,还可用backward(),back()

#定义利用datetime模块中的datetime.weekday()方法返回星期几(0,1,2..6),再通过读列表转成英文的函数
def wochentag(t): #形参t,当天的日期与时间实例
    wochentag = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"] #从星期一到星期天排列的英文列表
    return wochentag[t.weekday()] #返回对应的星期几英文列表元素

#定义利用datetime模块中的实例属性(只读),返回符合英文年月日书字规范的字符串函数
def datum(t): #形参t,当天的日期与时间实例
    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."] #从1月到12月排列的英文列表
    y = t.year #读取实例属性年数
    m = monat[t.month - 1] #读取实例属性月数,减1后再读取列表对应元素,获取该月英文缩略字符串
    d = t.day #读取实例属性天数
    #return "%s %d %d" % (m, d, y) #按字符串格式返回符合英文年月日书字规范的字符串
    return "{} {} {}".format(m, d, y) #按字符串格式返回符合英文年月日书字规范的字符串,等效前一条语句

#定义时钟走动(滴答,动画效果)函数 (注意时钟单位换算：1秒=1000毫秒  1毫秒=1000微秒  1秒=1000000微秒)
def tick():
    t = datetime.datetime.today() #返回表示当前地方时的datetime对象,日期与时间实例,注意句点表示法
    #sekunde = t.second + t.microsecond*0.000001 #t.second读取实例属性秒数据,值范围0-60
    sekunde = t.second + t.microsecond/1000000 #t.microsecond读取实例属性微秒数据,值范围0-1000000
    minute = t.minute + sekunde/60.0 #t.minute读取实例属性分数据,值范围0-60
    stunde = t.hour + minute/60.0 #t.hour读取实例属性时数据,值范围0-24
    try: #处理try-except之间代码块如果运行出错则运行pass部份所示的代码
        turtle.tracer(False) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(0)等效
        writer.clear() #删除writer海龟画笔绘图,实际为时钟面显示的星期几和年月日
        writer.home() #writer画笔回原点
        writer.forward(65) #writer画笔前进65,还可用fd()
        #调自定义wochentag()函数返回星期几的英文字符串并显示
        writer.write(wochentag(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.back(150) #writer画笔后退150,还可用backward(),bk()
        #调自定义datum()函数返回年月日的英文字符串并显示
        writer.write(datum(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(85) #writer画笔前进85(画笔回原点),还可用fd()
        #turtle.tracer(True) #恢复启用/禁用动画设置函数,还可用tracer(1)等效
        second_hand.setheading(6*sekunde) #设置海龟对象second_hand的朝向,秒针,每秒=6度
        minute_hand.setheading(6*minute) #设置海龟对象minute_hand的朝向,分针,每分=6度
        hour_hand.setheading(30*stunde) #设置海龟对象hour_hand的朝向,时针,每小时=30度
        turtle.tracer(True) #恢复启用/禁用动画设置函数,还可用tracer(1)等效
        turtle.ontimer(tick, 100) #定时器函数ontimer(),调用的函数必须是无参数,100毫秒后调用函数自身tick
    except turtle.Terminator: #处理turtle.Terminator异常对象
        pass  # turtledemo user pressed STOP

#程序主函数main()
def main():
    turtle.bgcolor('#85BE83') #设置绘画窗口背景色,调色参数获取可见color_rgb.py
    #下边tracer(False)语句可用#注释掉后,画图过程变慢,可观看到钟面设置画图过程
    turtle.tracer(False) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(0)等效
    setup() #调自定义时钟各指针及书写画笔初始设置函数
    #turtle.tracer(True) #恢复启用/禁用动画设置函数,还可用tracer(1)等效,  本命令在本程序中可省略
    tick() #调自定义时钟走动(滴答,动画效果)函数
    turtle.listen() #设置焦点接受按键亊件,下边是事件驱动(event-driven)语句
    turtle.onkeypress(turtle.bye,"q") #按键盘q键调用Screen()的专有方法bye(),退出程序运行
    turtle.onkeypress(turtle.bye,"Q") #按键盘Q键调用Screen()的专有方法bye(),退出程序运行
    return "clock_2.py:   main() END  EVENTLOOP"

#程序实际执行起点
if __name__ == "__main__":
    turtle.mode("logo") #设置海龟logo模式,海龟初始朝上,正数角度是顺时方向转,与时钟一致
    msg = main() #调用程序主函数main()
    print(msg) #在Python shell窗口或界面打印
    turtle.mainloop() #调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句