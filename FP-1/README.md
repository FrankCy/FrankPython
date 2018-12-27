# FP-1 第一章内容练习 #

- FP_Basic_Grammar.py
基础语法练习

- FP_Turtle_Drawing.py
绘图

- FP_What_Is_Name.py
简单的打招呼

- FP_String.py
字符串练习

## Python 基础语法 ##

### 输出 ###
```
print("Hello, World!")
print(2+2)
print(5000+5000)
```
### 输出乘除法 ###
```
# 需要除法运算，要加上下line-2这行，类似导包
from __future__ import division
print(1%1)
print(1*5)
#结果向下圆整，取余
print(10//3)
print(10%3)
print(9%3)
print(2.75%0.5)
```
### 交互式解释器执行 ###
```
y = input("The meaning of life :")
print(y)
#计算 手动输入的x和y的乘积
x = input("x: ")
y = input("y: ")
print(int(x) * int(y))
```

### 简单的逻辑判断 ###
```
# if（简） 语句
if 1 == 2 : print("One equals two")
if 1 == 1 : print("One equals one")
```
### 简单的函数运算 ###
```

# 函数练习
# 原来执行幂运算
print(2 ** 3)

# 运用函数
print(pow(2, 3))

# abs计算绝对值、round将浮点数圆整为与之最接近的整数
abs(-10)
round(2 / 3)
```
通常将pow等标 准函数称为内置函数，这类函数还有很多 —— [Python 函数介绍](#)，需要注意的是```Python round函数圆整是向下圆整，比如32.9，得32```。

### 模块 ###
```
#导入模块math
import math
#使用math，floor获取了这个数最小的整数，即32
math.floor(32.9)
```
 为表示出模块的作用，这里以module.function的形式展示了模块.方法调用方式，实际开发中我们可以用int(32.9)方式获取32这个值，无需引用模块。
```
#模块math还包含其他几个很有用的函数
#ceil传递32.3获取最大的即33
math.ceil(32.3)
#ceil传递32获取32
math.ceil(32)
```
实际开发过程中，为节省资源不导入不必要的函数，可以这么写：
```
#导入math模块的sqrt函数，计算平方根得3
from math import sqrt
sqrt(9)
```
### cmath和复数 ###
```
from math import sqrt
#获取-1的平方根，返回
#Traceback (most recent call last):
#...
#ValueError: math domain error
sqrt(-1)
#部分平台会返回
#nan
```
nan具体特殊含义，指“非数值”（not a number)。

### 海龟绘图 ###
```
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
```
海龟绘图，执行输出个图彩色螺旋线图（如果想了解更多，上Google或百度搜索 Python海龟绘图）

### 命令行执行Python ###
首先配置环境变量python（windows python.ext ／ UNIX python）
```
python hello.py
```
直接执行即可，还可以不使用python，直接使用hello.py执行程序，这里就不赘述了。

### 注释 ###
- “#“
```
# 打印圆的周长:
print(2 * pi * radius)
```

### 字符串 ###
#### 基础字符 ####
```
#单引号
print('Hello, world!')
#双引号
print("Hello, world!")
#字符串拼接
print("\"Hello, world!\" she said")
#单引号括双引号，输出与字符串拼接一致
print('"Hello, world!" she said')
```
#### 拼接字符 ####
```
#单引号
print('Hello, world!')
#双引号
print("Hello, world!")
#字符串拼接
print("\"Hello, world!\" she said")
#单引号括双引号，输出与字符串拼接一致
print('"Hello, world!" she said')

#字符拼接，包含单引号，repr是一个函数
print(repr("Hello,\nworld!"))

#字符拼接，包含单引号，str是一个会把\n认为是一个换行符
print(str("Hello,\nworld!"))

#大字符串表示 使用三引号 '''
print('''This is a very long string. It continues here. And it's not over yet. "Hello, world!" Still here.''')

#大字符串表示 使用三双引号 """ xxxx """
print("""This is a very long string. It continues here. And it's not over yet. "Hello, world!" Still here.""")

#输出盘符，因为盘符包含"\"，识别的时候会有问题
print("c:\abc.py")
print("c:\\abc.py")
#r的作用
print(r"c:\abc.py")
print(r'C:\Program Files\foo\bar' '\\')

#输出Unicode
print("\u00C6")
print("\U0001F60A")
print("This is a cat: \N{Cat}")

#转码
print("Hello, world!".encode("ASCII"))
print("Hello, world!".encode("UTF-8"))
print("Hello, world!".encode("UTF-32"))
#转码长度
print(len("How long is this?".encode("UTF-8")))
print(len("How long is this?".encode("UTF-32")))

# print("Hællå, wørld!".encode("ASCII")) 这行有错误 —— 斯堪的纳维亚字母没有对应的ASCII编码。
print("Hællå, wørld!".encode("ASCII", "ignore"))
print("Hællå, wørld!".encode("ASCII", "replace"))
print("Hællå, wørld!".encode("ASCII", "backslashreplace"))
print("Hællå, wørld!".encode("ASCII", "xmlcharrefreplace"))
print("Hællå, wørld!".encode())
print(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!'.decode())
#设置字符编码
print(bytes("Hællå, wørld!", encoding="utf-8"))
print(str(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!', encoding="utf-8"))

#bytearray
x = bytearray(b"Hello!")
x[1] = ord(b"u")
x
bytearray(b'Hullo!')
```

### 本文中出现的函数 ###
|函数|解释|
|:-|:-|
|abs(number)|返回指定数的绝对值|
|bytes(string, encoding[, errors])|对指定的字符串进行编码，并以指定的方式处理错误|
|cmath.sqrt(number)|返回平方根;可用于负数|
|float(object)|将字符串或数字转换为浮点数|
|help([object])|提供交互式帮助|
|input(prompt)|以字符串的方式获取用户输入|
|int(object)|将字符串或数转换为整数|
|math.ceil(number)|以浮点数的方式返回向上圆整的结果|
|math.floor(number)|以浮点数的方式返回向下圆整的结果|
|math.sqrt(number)|返回平方根;不能用于负数|
|pow(x, y[, z])|返回x的y次方对z求模的结果|
|print(object, ...)|将提供的实参打印出来，并用空格分隔|
|repr(object)|返回指定值的字符串表示|
|round(number[, ndigits])|四舍五入为指定的精度，正好为5时舍入到偶数|
|str(object)|将指定的值转换为字符串。用于转换bytes时，可指定编码和错误处理方式|
