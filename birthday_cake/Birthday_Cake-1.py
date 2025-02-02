# Birthday_Cake-1.py 绘制生日蛋糕程序. 本程序的的优化和被其它程序导入应用的改写版详见 Birthday_Cake.py
import turtle #导入python自带turtle模块，以便调用本模块的对象和函数等功能绘图
import math #导入python自带的数学函数库math

#创建无移动笔迹线函数
def noTraceGoto(x=0,y=0,angle=0):   #有三个形参分别是横坐标x值,垂直坐标y值,角度angle,黙认值均等于0
    turtle.pu()     # 抬起画笔,这样移动画笔到下一个绘图起始点的过程中不留笔迹线条,还可用penup(),up()
    turtle.goto(x,y)  # 移动海龟画笔到坐标x,y位置准备绘图,还可用setpos()
    turtle.setheading(angle)    #还可用seth(),将画笔朝向转到angle角度位,黙认值是标准模式时0,向屏幕右(东),
    turtle.pd()   # 放下画笔准备画图, 还可用pendown() ; down()
#创建画方形图函数,四个形参:第一条边长width1,第二条边长height2,是否填色coloring,画图方向turn
def drawRectangle(width1, height2,coloring=False,turn='left'):
    if coloring == True : #如coloring是True则开始准备填充颜色
        turtle.begin_fill()
    for i in range (2): #开始for循环2次画方形四个边
          turtle.forward(width1) #第一次循环画第一边第二次循环画第三边
          if turn == 'right' or turn == 'Right' : #如turn是'right',则画完一边画笔向右转90度
              turtle.right(90)
          else: #否则,则画完一边画笔向左转90度
              turtle.left(90)
          turtle.forward(height2) #第一次循环画第二边第二次循环画第四边
          if turn == 'right' or turn == 'Right' : #如turn是'right',则画完一边画笔向右转90度
              turtle.right(90)
          else: #否则,则画完一边画笔向左转90度
              turtle.left(90)
    if coloring == True : #如coloring是True则填充颜色完成
        turtle.end_fill()
    turtle.setheading(0) #画笔朝向回到初始方向,向屏幕右边

#创建画5角星函数,二个形参:size五角星对角线长度,2的整倍数.是否填色coloring,布尔变量
def fivePointedStar(size,coloring=False):
  x = size/2 #启笔是从五角星对角边中间开始画,故取size的二分之一
  if coloring == True : #如coloring是True则开始准备填充颜色
    turtle.begin_fill()
  turtle.right(144) #画笔从初始朝向右转144度
  for i in range(5): #for循环5次画五角星
        turtle.forward(x) #画x长直线
        turtle.right(144) #画笔向右转144度
        turtle.forward(x)
  if coloring == True : #如coloring是True则填充颜色完成
    turtle.end_fill()
  turtle.setheading(0) #画笔朝向回到初始方向,向屏幕右边

#创建画蛋糕奶油装饰层函数  其7个行参与下边调用waveformGraph_x()函数一致，详见selfTurtleModule.py
def creamCakeLayer(x,y,width=246,adjustment=0,amplitude=10,frequency=2,coefficient=100):
  turtle.begin_fill()
  turtle.goto(x-3,y) #蛋糕装饰层应比蛋糕大6,看起是盖在蛋糕上,对称就是x坐标每边大3
  turtle.goto(x-3,y-15) #向下包装蛋糕15
  waveformGraph_x(x-3,y-15,width,adjustment,amplitude,frequency,coefficient) #在此坐标位开始横向画波纹线条
  turtle.setheading(90) #画笔朝向回到初始方向,向屏幕右边
  turtle.goto(turtle.xcor(),y) #让尾笔近似图出与起笔对称收尾线,xcor()获取现时画笔x坐标
  turtle.goto(x-3,y) #回到画线起点,画出装饰层上边那条横线
  turtle.end_fill()

#画波形图函数,沿X轴水平方向,从左到右画图,有六个形参,后三个参数是对波形调整,注意取值范围,详见selfTurtleModule.py
def waveformGraph_x (x,y,width=246,adjustment=0,amplitude=10,frequency=2,coefficient=100):
  turtle.penup()
  turtle.goto(x,y) #开始画图坐标x,y起点
  turtle.setheading(0) #画笔指向角度0,朝右
  turtle.pendown()
  z=-width/2 #波形图宽度值的二分之一取负,是波形图最左边起点波形计算值,负正分二段后其图形左右才会是对称
  for i in range(x,width+x):#循环画波形,从起点x坐标开始,达波形宽度值结束,width+x是当x坐标不是原点0时,保证波形宽度值不变
    turtle.goto(i,y+adjustment-amplitude*math.cos((z/coefficient)*frequency*math.pi)) #y坐标就是波形计算值,函数math.cos()返回(z/coefficient)*frequency*math.pi弧度的余弦值,math.pi是常数圆周率
    z=z+1 #每循环一次z变量增加1,代入上边计算公式参与计算并画波形线条中的一个点
  turtle.goto(turtle.xcor(),y) #让尾笔近似图出与起笔对称收尾线,xcor()获取现时画笔x坐标

#开始调用上述自建函数画出1个蛋糕图形
if __name__ == "__main__":   # execute only if run as a script,模块可以通过检查自己的 __name__ 来得知是否运行在 main 作用域中，这使得模块可以在作为脚本或是通过 python -m 运行时条件性地执行下边代码，而在被 import 时不会执行
    turtle.pensize(1)    # 画笔粗细尺寸设置1    还可用还可用width()
    turtle.speed(1)     # 画笔画图速度设置 1最慢,速度关系按1,2,3,4,5,6,7,8,9,0排列  最快是0
    turtle.bgcolor('DeepSkyBlue') #设置绘画窗口背景色,#69D9FF,DeepSkyBlue
    y = -140 #蛋糕起笔计算坐标y初始值
    x = 0 #蛋糕起笔计算坐标x初始值
    #画最下边白色盘子
    turtle.color('white') #设置画笔和充填颜色,white白色,bisque
    noTraceGoto(x-150,y-10,0) #无痕迹移动画笔到坐标x-150,y-10  画笔朝初始方向,朝右
    drawRectangle(300, 10,True) #调画方形函数画盘子长300高10,充填白色
    #画盘子上的第1层巧克力色蛋糕 (最底层蛋糕)
    x = x-120 #定义画最底层蛋糕的坐标x,底层蛋糕宽是240,故两边对称就是-120到+120
    noTraceGoto(x,y,0)
    turtle.color('saddlebrown') #巧克力色十六进制码#BF671F, sienna,saddlebrown
    drawRectangle(240, 36,True) #调画方形函数画第1层巧克力色蛋糕长(宽)240高(厚)30,充填巧克力色
    #画第2层蛋糕
    y=y+36 #计算出在第一层36高的蛋糕上,画第2层蛋糕起点坐标y,x坐标不变
    noTraceGoto(x,y)
    turtle.color('pink')
    drawRectangle(240, 38,True) #调画方形函数画第2层蛋糕长(宽)240高(厚)38,充填pink色
    #画第2层蛋糕上的奶油装饰波形花纹层
    y=y+38 #计算出在第2层38高的蛋糕上,画装饰波形花纹层起点坐标y,x坐标不变
    turtle.color('white') #设置画笔和充填颜色,white白色,bisque
    noTraceGoto(x,y,0)
    creamCakeLayer(x,y,246,0,10,5,100) #调画蛋糕奶油装饰层函数画出装饰
    #画第3层蛋糕
    x=x+20 #计算出在第2层装饰波形花纹上,画第3蛋糕起点坐标x,y坐标不变
    noTraceGoto(x,y,0)
    turtle.color('saddlebrown') #巧克力色十六进制码#BF671F, sienna,saddlebrown
    drawRectangle(200, 28,True) #调画方形函数画第3层蛋糕长(宽)200高(厚)28,充填巧克力色
    #画第4层蛋糕
    y+=28 #等同于y=y+28
    noTraceGoto(x,y,0)
    turtle.color('pink')
    drawRectangle(200, 38,True) #调画方形函数画第4层蛋糕长(宽)200高(厚)35,充填pink色
    #画第4层蛋糕上的奶油装饰波形花纹层
    y+=38 #等同于y=y+38
    turtle.color('white') #设置画笔和充填颜色,white白色,bisque
    noTraceGoto(x,y,0)
    creamCakeLayer(x,y,206,0,10,3,150) #调画蛋糕奶油装饰层函数画出装
    #画第5层蛋糕
    x+=30 #等同于x=x+30
    noTraceGoto(x,y,0)
    turtle.color('saddlebrown') #巧克力色十六进制码#BF671F, sienna,saddlebrown
    drawRectangle(140, 28,True) #调画方形函数画第5层蛋糕长(宽)140高(厚)28,充填巧克力色
    #画第6层蛋糕
    y+=28 #等同于y=y+28
    turtle.color('pink') #设置画笔和充填颜色
    noTraceGoto(x,y,0)
    drawRectangle(140, 38,True) #调画方形函数画第6层蛋糕长(宽)140高(厚)38,充填pink色
    #画第6层蛋糕上的奶油装饰波形花纹层
    y+=38
    turtle.color('white') #设置画笔和充填颜色,white白色,bisque
    noTraceGoto(x,y,0)
    creamCakeLayer(x,y,146,-4,6,5,100) #调画蛋糕奶油装饰层函数画出装
    #画蛋糕顶上正中处蜡烛
    x+=66
    turtle.color('green') #设置画笔和充填颜色#93c572,limegreen
    noTraceGoto(x,y,0)
    drawRectangle(8, 66,True) #调画方形函数画蜡烛长(宽)8高66,充填色
    #画蜡烛头的5角星
    y+=66
    x+=6
    turtle.color('red')
    noTraceGoto(x,y,0)
    fivePointedStar(18,True) #调用自创建画5角星函数

    turtle.ht() #隐藏画笔
    turtle.mainloop() #还可用done(),必须作为一个海龟绘图程序的结束语句