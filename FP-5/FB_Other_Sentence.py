##条件、循环及其他语句

# ------------- 再谈print和import -------------
# 打印多个参数
## 以"，"号间隔
print('Age:', 42)
## 还可以这样写
name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello,'
print(name, salutation, greeting)
## 添加一个逗号
print(greeting, ',', salutation, name)
## 上面的语句会增加一个空格，我们可以用下面的语句替代
print(greeting + ',', salutation, name)
## 也可以动态添加分隔符（用于生成一个特定格式的字符，如每个参数之间有下划线的字符_，后续用于数组处理）
print("I", "wish", "to", "register", "a", "complaint", sep="_")
## 定义结束字符串
print("hello,", end=' ')
print("is me")

# 导入包时重命名
## 我们在导入包的时候如何做：
#import somemodule
## 或者
#from somemodule import somefunction
## 或者
#from somemodule import somefunction, anotherfunction, yetanotherfunction
## 也可以全部导入
#from somemodule import *
## ---- 可是在实际应用中，我们可能会遇到导入相同包名但情况，那我们如何解决呢 ----
# 给引用包起个别名 'as'
#import math as foobar
#print(foobar.sqrt(4))
# 导入特定函数并给它指定别名的例子
#from math import sqrt as foobar
#print(foobar(4))
# 如此，相同的包我们就可以起不同的别名了
#from module1 import open as open1
#from module2 import open as open2

# ------------- 赋值魔法 -------------
## 序列解包
# 同时给多个变量赋值
x,y,z = 1, 2, 3
print(x, y, z)
# 交换多个参数值（把x变为y，反之亦然）
x, y = y, x
print(x, y, z)
# 序列解包（可迭代对象解包），下面直接输出了该序列的位置
values = 1,2,3
print(values)
x,y,z = values
print(x)
print(y)
print(z)
# 获取最后一个键值，可以这样实现
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key)
print(value)
# 要解包的序列包含的元素个数必须对等，否则Python会异常：
# x,y,z=1,2
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module> ValueError: need more than 2 values to unpack >>>x,y,z=1,2,3,4
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module> ValueError: too many values to unpack
# 可以使用 "*" 来收集多余的值，这样无需确保值和变量的个数相同。
a,b,*rest=[1,2,3,4]
print(rest)
# 还可以将 "*" 号变量放到其他位置
name = "Albus Percival Wulfric Brian Dumbledore"
first, *middle, last = name.split()
print(middle)
# 赋值语句右边可以是任何类型的序列，但带"*"号的变量最终包含的是一个列表，变量和值的个数相同时也是如此：
a, *b, c = "abc"
print(a, b, c)

# 链式赋值
# x = y = somefunction()
# # 上述代码与下面的代码等价
# x = y = somefunction()
# x = y
# # 注：这两条语句与下述代码|不|对等
# x = somefunction()
# y = somefunction()

# 增强赋值
x=2
x+=1
print(x)
x*=2
print(x)
x/=2
print(x)
#其他的使用方式
fnord = 'foo'
fnord += 'bar'
print(fnord)
fnord *= 2
print(fnord)

# ------------- 代码块：缩进的乐趣 -------------
# 代码块不是语句，是Python的一个规范，可使用制表符来缩进代码。Python将制表符解释为移动到下一个制表位（相邻制表位相距8个空格），但标准（最佳的）做法是只使用空格（而不使用制表符）来缩进，且每级缩进4个空格。

# ------------- 条件和条件语句 -------------
# 布尔
print(True)
print(False)
print(True == 1)
print(False == 0)
print(True + False + 42)
#布尔值True和False属于类型bool，而bool与list、str和tuple一样，可用来转换其他的值。
print(bool('I think, therefore I am'))
print(bool())
print(42)
print(0)

# 有条件第执行if语句
#判断键入第值是不是Gumby
name = input('What is your name? ')
if name.endswith('Gumby'):
    print('Hello, Mr. Gumby')

# else子句
name = input('What is your name?')
if name.endswith('Gumby'):
    print('Hello, Mr. Gumby')
else:
    print('Hello, stranger')
#条件表达式
status = "friend" if name.endswith("Gumby") else "stranger"
print(status)

# elif子句
num = int(input('Enter a number: '))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')

# 代码块嵌套
name = input('What is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello, Mr. Gumby')
    elif name.startswith('Mrs.'):
        print('Hello, Mrs. Gumby')
    else:
        print('Hello, Gumby')
else:
    print('Hello, stranger')

# 更复杂的条件



