#Rainbow-0.py 彩虹绘制,网上下载版,未修改,仅对其语句进行了注释供参考,可参考另外几个版本Raindow_1,2,3,4,5.py
from turtle import *    #导入turtle模块,星号*，则在模块中定义的全部公有名称都将按 import 语句所在的作用域被绑定到局部命名空间
                        #在该调用模块内直接按turtle定义的名称使用其对象和函数
                        #不需要指明调用函数的从属关系

# 创建for循环画100次园的调色函数,RGB值分成6段调值变化:赤橙黄绿青蓝紫变化排列
def HSB2RGB(hues):
    hues = hues * 3.59 #本程序是循环画100,转成0-359范围能等分成6段(每段为60),所乘系数=359/循环画的总次数(359/100=3.59)
    rgb=[0.0,0.0,0.0] # 设RGB初始值
    i = int(hues/60)%6 #次数hues除以60取整数后,再除以6取余数(范围应是0,1,2,3,4,5),确定每次调色的段
    f = hues/60 -i #调整值f,次数hues除以60再减去该调色段数是一个范围在0-1之间的变化数,与循环次数相关联
    if i == 0: #0段,R=1 G由0渐调(增加)到1 B=0,颜色变化：红渐变到橙再渐变到黄
        rgb[0] = 1; rgb[1] = f; rgb[2] = 0
    elif i == 1: #1段,R由1渐调(减少)到0 G=1 B=0,颜色变化：黄渐变化到绿
        rgb[0] = 1-f; rgb[1] = 1; rgb[2] = 0
    elif i == 2: #2段,R=0 G=1 B由0渐调(增加)到1,颜色变化：绿渐变到青
        rgb[0] = 0; rgb[1] = 1; rgb[2] = f
    elif i == 3: #3段,R=0 G由1渐调(减少)到0 B=1,颜色变化：青渐变化到蓝
        rgb[0] = 0; rgb[1] = 1-f; rgb[2] = 1
    elif i == 4: #4段,R由0渐调(增加)到1 G=0 B=1,颜色变化：蓝渐变到紫
        rgb[0] = f; rgb[1] = 0; rgb[2] = 1
    elif i == 5: #5段,R=1 G=0 B由1渐调(减少)到0,颜色变化：紫渐变化到红
        rgb[0] = 1; rgb[1] = 0; rgb[2] = 1-f
    return rgb #本函数返回列表变量rgb的值(RGB)

#绘制彩虹函数
def rainbow():
    hues = 0.0 #色调变量初始化
    color(1,0,0) #设置画笔颜色,RGB值,红色
    hideturtle() #隐藏海龟画笔,ht()
    speed(6) #画笔画图速度设置
    pensize(3) #画笔粗细尺寸设置
    penup() #抬起画笔
    goto(-650,-150) #画彩虹起始坐标位
    #goto(-50,-50) #
    pendown() #放下画笔
    right(110) #画笔朝向向右转110
    for i in range (100): #for循环,画100次园
        circle(600)  #调画园函数画园,圆的半径600
        right(0.23) #每画一个园画笔朝向向右转0.23
        hues = hues + 1 #每画一个园色调变量加1
        rgb = HSB2RGB(hues)
        #color(rgb[0],rgb[1],rgb[2]) #设置画笔颜色,RGB值
        color(rgb)  #设置画笔颜色,RGB值
    penup() #抬起画笔

def main():
    #setup(1200, 800, 0, 0)
    setup(1200, 800) #s
    #bgcolor((64/255, 64/255, 1))
    #tracer(False)
    #tracer(1) #s
    tracer(0) #s
    rainbow()
    #输出文字
    tracer(False)
    goto(0,0)
    pendown()
    color('yellow')
    write("彩虹",align="center",
    font=("Script MT Bold", 80, "bold"))
    tracer(True)


if __name__ == "__main__":
    main()
    mainloop()