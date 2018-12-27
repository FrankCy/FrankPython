#海龟绘图，执行输出个图（如果想了解更多，上Google或百度搜索 Python海龟绘图）

#彩色螺旋线
import turtle
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red","yellow","purple","blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
turtle.done()
