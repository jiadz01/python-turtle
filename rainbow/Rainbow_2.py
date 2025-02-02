"""绘画彩虹 Rainbow_2.py 可供其它程序导入,调用rainbow绘画彩虹函数,模块最后有一运行简单演示部份
本程序是在Rainbow_1.py的基础改进,改变调色算法(另一种算法),能任意调整不同色段所占彩虹总厚度的比例
自定义2个函数:
- rgbPalette()函数,RGB的调色函数,RGB值分成6段调值变化:赤-橙-黄-绿-青-蓝-紫-赤渐变化排列
    调色原理详见advanced_colormixer.py
    segment 整数参数,色段,取值范围:0,1,2,3,4,5
    hues 浮点数参数,色调变化值,取值范围0.00-1.00

- rainbow()函数,绘画彩虹,有8个形参:
    X 横坐标值
    Y 垂直坐标值
    width 整数参数,绘制彩虹厚度(画多少次圆弧),默认值=100,可取值30-200
    radius 整数参数,彩虹圆弧半径,默认值=100,可取值30-500
    axial 字符串变量,画彩虹时每画一次画笔移动轴向,默认值='y'(沿y轴减少), 可取值'x'(沿x轴减少)或'y'
    extent 彩虹弧长的园弧夹角,默认值=180,可取值45-360
    towards 画笔起始方向,默认值=90,可取值0-359,常用0,90,180,270
    size 画笔粗细尺寸(每画一次),默认值=1,可取值1,2,3
"""
import turtle   #导入turtle模块，调用其对象和函数等功能

# 创建RGB的调色函数,RGB值分成6段调值变化:赤橙黄绿青蓝紫赤变化排列,有2个形参
def rgbPalette(segment,hues): #形参segment色段,取值范围0,1,2,3,4,5   形参hues色调变化值,取值范围0.00-1.00
    rgb=[0.0,0.0,0.0] # 设RGB初始值,列表变量
    if segment == 0: #0段,R=1 G由0渐调(增加)到1 B=0,颜色变化：红渐变到橙再渐变到黄
        rgb[0] = 1; rgb[1] = hues; rgb[2] = 0 #RGB列表变量赋值,调色
    elif segment == 1: #1段,R由1渐调(减少)到0 G=1 B=0,颜色变化：黄渐变化到绿
        rgb[0] = 1-hues; rgb[1] = 1; rgb[2] = 0
    elif segment == 2: #2段,R=0 G=1 B由0渐调(增加)到1,颜色变化：绿渐变到青
        rgb[0] = 0; rgb[1] = 1; rgb[2] = hues
    elif segment == 3: #3段,R=0 G由1渐调(减少)到0 B=1,颜色变化：青渐变化到蓝
        rgb[0] = 0; rgb[1] = 1-hues; rgb[2] = 1
    elif segment == 4: #4段,R由0渐调(增加)到1 G=0 B=1,颜色变化：蓝渐变到紫
        rgb[0] = hues; rgb[1] = 0; rgb[2] = 1
    elif segment == 5: #5段,R=1 G=0 B由1渐调(减少)到0,颜色变化：紫渐变化到红
        rgb[0] = 1; rgb[1] = 0; rgb[2] = 1-hues
    return rgb #本函数返回列表变量rgb的值(RGB)

#绘制彩虹函数,带有8个形参
def rainbow(x,y,width=100,radius=100,axial='y',extent=180,towards=90,size=1):
    visible = turtle.isvisible() #测试原海龟笔是否可见,显示返回True,隐藏返回False,布尔变量
    turtle.speed(0) #画笔画图速度设置,1最慢,速度关系按1,2,3,4,5,6,7,8,9,0排列  最快是0
    turtle.hideturtle() #隐藏海龟画笔,ht()
    pensize = turtle.pensize()    #变量pensize保留当前海龟画笔粗细设置,    还可用还可用width()
    turtle.pensize(size) #画笔粗细尺寸设置
    turtle.penup() #抬起画笔
    turtle.goto(x,y) #画彩虹起始坐标位
    turtle.pendown() #放下画笔
    turtle.color(1,0,0) #设置画笔颜色,RGB值,彩虹初始绘制红色
    #彩虹只需5段色(赤橙黄绿青蓝紫),本例0段占彩虹总厚度40%,1,2,3,4段各段占15%,确保各段比例之和=100%
    segment1 = int(width*0.4)-1 #0段(红渐变到橙再渐变到黄)次数结束数(也是1段起始的次数),占彩虹总厚度40%
    segment2 = int(width*0.15)+segment1 #2段(绿渐变到青)起始的次数,占彩虹总厚度15%
    segment3 = int(width*0.15)+segment2 #3段(青渐变化到蓝)起始的次数,占彩虹总厚度15%
    segment4 = int(width*0.15)+segment3 #4段(蓝渐变到紫)起始的次数,占彩虹总厚度15%
    segment = 0 #设置色段参数变量为0段(彩虹初始绘制红色)
    hues = 0 #设置色调变化值参数变量初始为0
    z = 1/segment1 #设置0段的每画一次的增量值,
    for i in range (width): #for循环,画实参变量width的值次数园,完成后退出循环（i=0....i=width-1)
        turtle.seth(towards) #设置画笔朝向
        turtle.circle(radius,extent)  #调画园函数画园,圆的半径radius,园弧夹角extent
        turtle.penup() #抬起画笔
        if axial == 'x' or axial == 'X': #判定画彩虹时的轴向参数是否是'x'
            x=x-size #是,每画一个园x轴坐标就向左移动画笔粗细大小的坐标位
        else:
            y=y-size #否,每画一个园y轴坐标就向下移动画笔粗细大小的坐标位(默认设置)
        turtle.goto(x,y) #画下一个彩虹(园)坐标位
        turtle.pendown() #放下画笔
        if i == segment1: #循环次=0段次数结束数(也是1段起始的次数)
            segment = 1 #设置色段参数变量为1段
            z = 1/int(width*0.15) #设置1段的每画一次的增量值
            hues = 0 #设置色调变化值参数变量初始为0
        elif i == segment2: #循环次=1段次数结束数(也是2段起始的次数)
            segment = 2 #设置色段参数变量为2段
            z = 1/int(width*0.15) #设置2段的每画一次的增量值
            hues = 0 #设置色调变化值参数变量初始为0
        elif i == segment3: #循环次=2段次数结束数(也是3段起始的次数)
            segment = 3 #设置色段参数变量为3段
            z = 1/int(width*0.15) #设置3段的每画一次的增量值
            hues = 0 #设置色调变化值参数变量初始为0
        elif i == segment4: #循环次=3段次数结束数(也是4段起始的次数)
            segment = 4 #设置色段参数变量为4段
            z = 1/int(width*0.15) #设置4段的每画一次的增量值
            hues = 0 #设置色调变化值参数变量初始为0
        else: #如果都不是则运行如下语句
            hues = hues + z #色调变化值=原值+每次增量值

        if hues >= 1: #确保调色变量值不得大于1而出错
            hues =1.00
        rgb = rgbPalette(segment,hues) #用上边参数调用RGB调色函数求出rgb值
        turtle.color(rgb)  #设置画笔RGB值颜色
    turtle.pensize(pensize)    #画笔回到调用前粗细设置
    if visible == True : #画笔回到调用前是否显示或隐藏状态
        turtle.showturtle()  #显示海龟笔.还可用st()
        turtle.seth(towards) #画笔回到设置画笔朝向
    turtle.penup() #抬起画笔

#运行本程序的自创函数简单演示部份,当本模块被其它程序导入时可自动识别而不会执行以下语句
if __name__ == "__main__": # execute only if run as a script
    #调自定义绘制彩虹函数绘图,可修改下边各调用实参数观察绘图变化
    rainbow(300,0,100,300) #调自定义绘制彩虹函数绘图,后边另4个参数选用默认值故可不填写实参数
    turtle.tracer(False) #启用/禁用动画并设置刷新延迟时间为0,这时后边画图速度很快,还可用tracer(0)等效
    rainbow(300,-200,100,200,'x') #调自定义绘制彩虹函数绘图,后边另3个参数选用默认值故可不填写实参数
    turtle.tracer(True) #恢复启用/禁用动画设置函数,还可用tracer(1)等效
    turtle.mainloop() #开始事件循环,调用 Tkinter的mainloop()函数,还可用done(),必须作为一个海龟绘图程序的结束语句