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
# name = input('What is your name? ')
# if name.endswith('Gumby'):
#     print('Hello, Mr. Gumby')
#
# # else子句
# name = input('What is your name?')
# if name.endswith('Gumby'):
#     print('Hello, Mr. Gumby')
# else:
#     print('Hello, stranger')
#条件表达式
status = "friend" if name.endswith("Gumby") else "stranger"
print(status)

# elif子句
# num = int(input('Enter a number: '))
# if num > 0:
#     print('The number is positive')
# elif num < 0:
#     print('The number is negative')
# else:
#     print('The number is zero')

# 代码块嵌套
# name = input('What is your name? ')
# if name.endswith('Gumby'):
#     if name.startswith('Mr.'):
#         print('Hello, Mr. Gumby')
#     elif name.startswith('Mrs.'):
#         print('Hello, Mrs. Gumby')
#     else:
#         print('Hello, Gumby')
# else:
#     print('Hello, stranger')

# 更复杂的条件
#比较运算符
##相等运算符
print("foo" == "foo")
print("foo" == "bar")
#错误语法
# print("foo"="foo")
##is相同运算符
x=y=[1,2,3]
z=[1,2,3]
print(x == y)
print(x == z)
print(x is y)
#is是相同值比较
print(x is z)

x=[1,2,3]
y=[2,4]
print(x is not y)

del x[2]
y[1] = 1
print(y.reverse())
print(x==y)
print(x is y)
#in成员资格运算符
# name = input('What is your name?')
# if 's' in name:
#     print('Your name contains the letter "s".')
# else:
#     print('Your name does not contain the letter "s".')
#字符串和序列的比较
#字符串是根据字符的字母排列顺序进行比较的。
print("alpha" < "beta")
#字母排列顺序比较
print("a" < "b")
#涉及大写字母时，排列顺序就可能与想要的不同
print("a" < "B")
#忽略大小写，再进行比较，但是要使用字符串方法lower()
print("a".lower() < "B".lower())
print('FnOrD'.lower() == 'Fnord'.lower())
#其他比较
print([1,2]<[2,1])
#其他序列比较
print([2, [1, 4]] < [2, [1, 5]])

#布尔运算符
#例：检查输入数值是否位于1～10（包含）。
# number = int(input('Enter a number between 1 and 10: '))
# if(number <= 10):
#     if number >= 1:
#         print("Great!")
#     else:
#         print("Wrong!")
# else:
#     print("Wrong!!!")
#上面的代码看着有些臃肿，我可以这样优化：
# number = int(input('Enter a number between 1 and 10: '))
# if number <= 10 and number >= 1:
#     print("Great!")
# else:
#     print("Wrong!")

# 断言
#当没有断言时的语句如下：
# age = 10
# assert 0 < age < 100
# age = -1
# assert 0 < age < 100
#添加断言的时的语句如下：
# age=-1
# assert 0 < age < 100, '发生错误，请联系管理员'

# -------------  循环 -------------
## while循环
x=1
while x <= 100:
    print(x)
    x += 1
#使用循环来确保用户输入名字，只有输入名字之后才会停止循环
# name = ''
# while not name:
#     name = input('Please enter your name: ')
# print('Hello, {}!'.format(name))

## for 循环
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

numbers = [0,1,2,3,4,5,6,7,8,9]
for number in numbers:
    print(number)

#一种创建范围的内置函数
range(0, 10)
list(range(0, 10))
print(list(range(0, 10)))

for number in range(1,101):
    print(number)

## 迭代字典
d={'x':1,'y':2,'z':3}
for key in d:
    print(key, 'corresponds to', d[key])

##d.items以元组的方式返回键值对。
for key, value in d.items():
    print(key, 'corresponds to', value)

## 一些迭代工具
###并行迭代
#研发过程中，如果遇到需要同时迭代两个序列，我们会怎么做呢？
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
#打印名字和对应多年龄，可以这样做
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')
#通过zip迭代函数将两个序列组合（书中叫'缝合'）
list(zip(names, ages))
print(list(zip(names, ages)))
#迭代
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
#当序列长度不一致时，函数zip将最短的序列用完后停止"缝合"
print(list(zip(range(5), range(100000000))))
strings = 'aksjdaldjalkjdxxxxxx'
#迭代时获取索引
#迭代判断并替换指定字符
for string in strings:
    if 'xxx' in string:
        index = strings.index(string)  # 在字符串列表中查找字符串
        strings[index] = '[censored]'
print(strings)
#优化语句块，返回该字符串首次出现的位置
index = 0
for string in strings:
    if 'xxx' in string:
        strings[index] = '[censored]'
    index += 1
print(index)
print(strings)
#上面返回该字符串首次出现的位置实现方式过于笨拙，我们可以使用内置函数enumerate
for index, string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[censored]'
print(index)
print(strings)
#反向迭代和排序后再迭代
#排序
print(sorted([4, 3, 6, 8, 3]))
print(sorted('Hello, world!'))
#反转序列
print(list(reversed('Hello, world!')))
print(''.join(reversed('Hello, world!')))

#跳出循环
##break，找出小于100的最大平方值（整数与自己相乘的结果），从100向下迭代。找到最大平方值后，无需再迭代，因此直接跳出循环。
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
#运行程序，n为81，range有3个参数 —— 步长，即序列中相邻数的差。通过将步长设置为负数，可让range向下迭代。
for n in range(0, 10, 2):
    print(n)
#continue
#跳转for循环
# for x in seq:
#     if condition1: continue
#     if condition2: continue
#     if condition3: continue

    # do_something()
    # do_something_else()
    # do_another_thing()
    # etc()
#要满足上面的结果，我们使用一个if就可以做到
# for x in seq:
#     if not (condition1 or condition2 or condition3) :
#         do_something()
#         do_something_else()
#         do_another_thing()
#         etc()
#while True/break示例
#如果用户一直输入值，则不断提示，让用户输入，否则停止
while True:
    word = input('Please enter a word: ')
    if not word: break
    # 使用这个单词做些事情:
    print('The word was ', word)

#循环中的else子句
#循环，break时直接执行else
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it!")

# ------------- 简单推导 -------------
#打印100个由平方组成的数
print([x * x for x in range(100)])
#打印这100个由平方组成的数，能被3整除的值
print([x*x for x in range(100) if x % 3 == 0])
#将首字母相同的男孩和女孩速配
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])
#优化速配代码，它的最佳实践是这样的
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
#通过字典推导，输出99的平方
squares = {i:"{} squared is {}".format(i, i**2) for i in range(100)}
print(squares[99])

# ------------- 三人行 -------------
##pass什么都不做
#错误示范，其中一个elif未完成，在执行时中会发生错误，导致程序无法运行
# if name == 'Ralph Auldus Melish':
#     print('Welcome!')
# elif name == 'Enid':
#     还未完成......
# elif name == 'Bill Gates':
#     print('Access Denied')

#通过pass作为占位符，让程序可以正常通过
if name == 'Ralph Auldus Melish':
    print('Welcome!')
elif name == 'Enid':
    # 还未完成......
    pass
elif name == 'Bill Gates':
    print('Access Denied')
##del
x = 1
del x
# print(x) 这行会报错，因为名称x被删除

x = ["Hello", "world"]
y = x
y[1] = "Python"
print(x)
#删除x，看看y的结果
del x
print(y)
#y依然存在