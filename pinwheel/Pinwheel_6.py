'''Pinwheel_6.py  演示从自编模块中导入函数的应用实例
本程序要导入自建的Pinwheel_4.py和Pinwheel_5.py模块,它们应与本程序同在一个文件目录内.
注意导入的rotateWindmill_5()只能在程序的最后才能运行,原因详见Pinwheel_5.py
'''
import turtle #导入turtle模块，调用其对象和函数等功能前加(turtle.)
from Pinwheel_4 import rotateWindmill_4 #从Pinwheel_4模块中导入画动画风车rotateWindmill_4()函数
from Pinwheel_5 import rotateWindmill_5 ##从Pinwheel_5模块中导入画动画风车rotateWindmill_5()函数

if __name__ == "__main__": # execute only if run as a script
    turtle.hideturtle() #隐藏海龟可加速绘画速度
    turtle.bgcolor(0.5,0.5,0.5) #设置绘画窗口背景色,调色参数获取可见color_rgb.py
    rotateWindmill_4(0,0,3) #调用Pinwheel_4模块中的函数在x=0,y=0坐标画风车,反时针旋转3圈
    rotateWindmill_4(0,0,3,True) #调用Pinwheel_4模块中的函数在x=0,y=0坐标画风车,顺时针旋转3圈
    rotateWindmill_4(190,90,2) #调用Pinwheel_4模块中的函数在x=190,y=90坐标画风车,反时针旋转2圈
    rotateWindmill_5(-100,0,3,True) #调用Pinwheel_5模块中的函数在x=-100,y=0坐标动画风车,顺时针旋转3圈

    turtle.done() #调用 Tkinter 的 mainloop 函数,必须作为一个海龟绘图程序的结束语句,还可用mainloop()