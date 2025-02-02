""" Birthday_Cake.py 绘制生日蛋糕,该模块可在绘图窗口任意坐标画出并可以被其它程序导入,是Birthday_Cake-1.py基础上改写优化版
-本程序要导入自建的 selfTurtleModule.py模块,它应与本程序同在一个文件目录内.导入4个自建函数:
    1.noTraceGoto()移动画笔无移动笔迹线函数
    2.drawRectangle()画方形图函数
    3.fivePointedStar()画5角星函数
    4.waveformGraph_x()沿X轴水平方向画波形图函数

-本程序创建窗口任意坐标绘生日蛋糕图的函数 birthdayCake(),可以被其它程序导入,有7个形参:
    X 横坐标值,黙认值=0
    Y 垂直坐标值,黙认值=-140
    plateColor字符串参数, 盘子颜色，黙认值='white'
    creamColor字符串参数, 奶油装饰层颜色，黙认值='white'
    cakeColor1字符串参数, 蛋糕1,3,5层颜色，黙认值='saddlebrown'
    cakeColor2字符串参数, 蛋糕2,4,6层颜色，黙认值='pink'
    candleColor字符串参数, 蜡烛颜色, 黙认值='green'
"""
import turtle #导入turtle模块，以便调用本模块的对象和函数等功能
from selfTurtleModule import noTraceGoto,drawRectangle,fivePointedStar,waveformGraph_x #从selfTurtleModule.py模块中导入4函数

#创建画蛋糕奶油装饰层函数,其7个行参与下边调用waveformGraph_x()函数一致，详见selfTurtleModule.py
def creamCakeLayer(x,y,width=246,adjustment=0,amplitude=10,frequency=2,coefficient=100):
  turtle.begin_fill()
  turtle.goto(x-3,y) #蛋糕装饰层应比蛋糕大6,看起是盖在蛋糕上,对称就是x坐标每边大3
  turtle.goto(x-3,y-15) #向下包装蛋糕15
  waveformGraph_x(x-3,y-15,width,adjustment,amplitude,frequency,coefficient) #在此坐标位开始横向画波纹线条
  turtle.setheading(90) #画笔朝向回到初始方向,向屏幕右边
  turtle.goto(turtle.xcor(),y) #让尾笔近似图出与起笔对称收尾线, xcor()获取现时画笔x坐标
  turtle.goto(x-3,y) #回到画线起点,画出装饰层上边那条横线
  turtle.end_fill()

#创建窗口任意坐标绘生日蛋糕图的函数,
def birthdayCake(x=0,y=-140,plateColor='white',creamColor='white',cakeColor1='saddlebrown',cakeColor2='pink',candleColor='green'):
    pensize = turtle.pensize()    #变量pensize保留当前海龟画笔粗细设置
    turtle.pensize(1)    # 画笔粗细尺寸设置1    还可用还可用width()
    #画最下边盘子
    turtle.color(plateColor) #设置盘子颜色,white白色,bisque
    noTraceGoto(x-150,y-10,0) #无痕迹移动画笔到坐标x-150,y-10  画笔朝初始方向,朝右
    drawRectangle(300, 10,True) #调画方形函数画盘子长300高10,充填白色
    #画盘子上的第1层巧克力色蛋糕 (最底层蛋糕)
    x = x-120 #定义画最底层蛋糕的坐标x,底层蛋糕宽是240,故两边对称就是-120到+120
    noTraceGoto(x,y,0)
    turtle.color(cakeColor1) #巧克力色十六进制码#BF671F, sienna,saddlebrown
    drawRectangle(240, 36,True) #调画方形函数画第1层巧克力色蛋糕长(宽)240高(厚)30,充填巧克力色
    #画第2层蛋糕
    y=y+36 #计算出在第一层36高的蛋糕上,画第2层蛋糕起点坐标y,x坐标不变
    noTraceGoto(x,y)
    turtle.color(cakeColor2)
    drawRectangle(240, 38,True) #调画方形函数画第2层蛋糕长(宽)240高(厚)38,充填pink色
    #画第2层蛋糕上的奶油装饰波形花纹层
    y=y+38 #计算出在第2层38高的蛋糕上,画装饰波形花纹层起点坐标y,x坐标不变
    turtle.color(creamColor) #设置画笔和充填颜色,white白色,bisque
    noTraceGoto(x,y,0)
    creamCakeLayer(x,y,246,0,10,5,100) #调画蛋糕奶油装饰层函数画出装饰
    #画第3层蛋糕
    x=x+20 #计算出在第2层装饰波形花纹上,画第3蛋糕起点坐标x,y坐标不变
    noTraceGoto(x,y,0)
    turtle.color(cakeColor1) #巧克力色十六进制码#BF671F, sienna,saddlebrown
    drawRectangle(200, 28,True) #调画方形函数画第3层蛋糕长(宽)200高(厚)28,充填巧克力色
    #画第4层蛋糕
    y+=28 #等同于y=y+28
    noTraceGoto(x,y,0)
    turtle.color(cakeColor2)
    drawRectangle(200, 38,True) #调画方形函数画第4层蛋糕长(宽)200高(厚)35,充填pink色
    #画第4层蛋糕上的奶油装饰波形花纹层
    y+=38 #等同于y=y+38
    turtle.color(creamColor) #设置画笔和充填颜色,white白色,bisque
    noTraceGoto(x,y,0)
    creamCakeLayer(x,y,206,0,10,3,150) #调画蛋糕奶油装饰层函数画出装
    #画第5层蛋糕
    x+=30 #等同于x=x+30
    noTraceGoto(x,y,0)
    turtle.color(cakeColor1) #巧克力色十六进制码#BF671F, sienna,saddlebrown
    drawRectangle(140, 28,True) #调画方形函数画第5层蛋糕长(宽)140高(厚)28,充填巧克力色
    #画第6层蛋糕
    y+=28 #等同于y=y+28
    turtle.color(cakeColor2) #设置画笔和充填颜色
    noTraceGoto(x,y,0)
    drawRectangle(140, 38,True) #调画方形函数画第6层蛋糕长(宽)140高(厚)38,充填pink色
    #画第6层蛋糕上的奶油装饰波形花纹层
    y+=38
    turtle.color(creamColor) #设置画笔和充填颜色,white白色,bisque
    noTraceGoto(x,y,0)
    creamCakeLayer(x,y,146,-4,6,5,100) #调画蛋糕奶油装饰层函数画出装
    #画蛋糕顶上正中处蜡烛
    x+=66
    turtle.color(candleColor) #设置画笔和充填颜色
    noTraceGoto(x,y,0)
    drawRectangle(8, 66,True) #调画方形函数画蜡烛长(宽)8高66,充填色
    #画蜡烛头的5角星
    y+=66
    x+=6
    turtle.color('red')
    noTraceGoto(x,y,0)
    fivePointedStar(18,True) #调用自创建画5角星函数
    turtle.pensize(pensize)    #画笔回到调用前粗细设置

#运行本程序的自创函数演示,当本模块被其它程序导入时可自动识别而不会执行以下语句
if __name__ == "__main__":   # execute only if run as a script,模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行下边代码，而在被 import 时不会执行
    turtle.speed(0)     # 画笔画图速度设置 1最慢,速度关系按1,2,3,4,5,6,7,8,9,0排列  最快是0
    turtle.bgcolor('DeepSkyBlue') #设置绘画窗口背景色,#69D9FF,DeepSkyBlue
    birthdayCake(180,-200) #调用上边的创建的画蛋糕函数画蛋糕，只传入画蛋糕起始坐标参数，其它省略,使用默认值
    birthdayCake(-180,-200,'blue','sienna','bisque','olive','gold') #调用上边的创建的画蛋糕函数画蛋糕,传入7个实参

    turtle.ht() #隐藏画笔
    turtle.mainloop() #还可用done(),必须作为一个海龟绘图程序的结束语句