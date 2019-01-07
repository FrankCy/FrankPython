# FP-3 第三章使用字符串 #

- FP_Setting_String_Pattern.py <br/>
设置字符串的格式 完整版

- FP_String_Basic_Operation.py <br/>
字符串基本操作

- FP_String_Method.py <br/>
字符串方法


# Python 使用字符串 #
本章将介绍如何使用字符串来设置其他值的格式(比如便于打印)，并大致了解使用字 符串方法可完成的重要任务，如拆分、合并和查找等

## 字符串基本操作 ##
```python
######## 字符串基本操作 ########
website = 'http://www.python.org'
website[-3:] = 'com'
# Traceback (most recent call last):
#        File "<pyshell#19>", line 1, in ?
# website[-3:] = 'com'
# TypeError: object doesn't support slice assignment
# 字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的，上面代码是错误的！
```

## 设置字符串的格式:完整版 ##
```python
######## 设置字符串的格式:完整版 ########
print("{{ceci n'est pas une replacement field}}".format())
```
在格式字符串中，最激动人心的部分为替换字段。替换字段由如下部分组成，其中每个部分 都是可选的。
- 字段名
索引或标识符，指出要设置哪个值的格式并使用结果来替换该字段。除指定值 外，还可指定值的特定部分，如列表的元素。
- 转换标志
跟在叹号后面的单个字符。当前支持的字符包括r(表示repr)、s(表示str) 和a(表示ascii)。如果你指定了转换标志，将不使用对象本身的格式设置机制，而是使 用指定的函数将对象转换为字符串，再做进一步的格式设置。
- 格式说明符
跟在冒号后面的表达式(这种表达式是使用微型格式指定语言表示的)。格 式说明符让我们能够详细地指定最终的格式，包括格式类型(如字符串、浮点数或十六 进制数)，字段宽度和数的精度，如何显示符号和千位分隔符，以及各种对齐和填充方式。

###  替换字段名 ###

```python
######## 替换字段名 ########
#顺序从左向右替换字符，但是指定了'bar'和'foo'的值，所以改变了原来顺序
print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))
#指定按列表序列指定，区别于上面，{1}代表2 {0}代表1
print("{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3))

#替换{name[1]}的参数，为fullname数组的第2个值
fullname = ["Alfred", "Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))

#导入包math，并实测替换
import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))
print(math.__name__)
print(math.pi)
```

### 基本转换 ###
```python
######## 基本转换 ########
#将pi替换成"π"
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))
#上述三个标志(s、r和a)指定分别使用str、repr和ascii进行转换。
#str：通常创建外观 普通的字符串版本(这里没有对输入字符串做任何处理)。
#repr：尝试创建给定值的Python表 示(这里是一个字符串字面量)。
#ascii：创建只包含ASCII字符的表示，类似于Python 2中的 repr。

#赋值（好像可以用到SQL，未来查证）
print("The number is {num}".format(num=42))
print("The number is {num:f}".format(num=42))
#并赋予其二进制处理
print("The number is {num:b}".format(num=42))
```
- 字符串格式设置中的类型说明符

| 类型 | 含义 |
|:-|:-|
| b | 将整数表示为二进制数 |
| c | 将整数解读为Unicode码点 |
| d | 将整数视为十进制数进行处理，这是整数默认使用的说明符 |
| e | 使用科学表示法来表示小数(用e来表示指数) |
| E | 与e相同，但使用E来表示指数 |
| f | 将小数表示为定点数 |
| F | 与f相同，但对于特殊值(nan和inf)，使用大写表示 |
| g | 自动在定点表示法和科学表示法之间做出选择。这是默认用于小数的说明符，但在默认情况下至少有1位小数 |
| G | 与g相同，但使用大写来表示指数和特殊值 |
| n | 与g相同，但插入随区域而异的数字分隔符 |
| o | 将整数表示为八进制数 |
| s | 保持字符串的格式不变，这是默认用于字符串的说明符 |
| x | 将整数表示为十六进制数并使用小写字母 |
| X | 与x相同，但使用大写字母 |
| % | 将数表示为百分比值(乘以100，按说明符f设置格式，再在后面加上%) |

### 宽度、精度和千位分隔符 ###
```python
pi = 1
print("{num:10}".format(num=3))
print("{name:10}".format(name="Bob"))
#如上所见，数和字符串的对齐方式不同，具体为什么请查看：
#pi被作为定点数
print("'Pi day is {pi:.2f}'".format(pi=pi))
print("{pi:10.2f}".format(pi=pi))
#替换字符"Guido van Rossum"获取前
print("{:.5}".format("Guido van Rossum"))
#使用逗号来指出你要添加千位分隔符
print('One googol is {:,}'.format(10**100))
```

### 符号、对齐和用0填充 ###
```python
print('{:010.2f}'.format(pi))

#要指定左对齐、右对齐和居中，可分别使用<、>和^。
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))

#使用填充字符来扩充对齐说明符，这样将使用指定的字符而不是默认的空格来填充
print("{:$^15}".format(" WIN BIG "))

#更具体的说明符=，它指定将填充字符放在符号和数字之间
print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi))
print('{0:10.2f}\n{1:=10.2f}'.format(pi, -pi))

#如果要给正数加上符号，可使用说明符+(将其放在对齐说明符后面)，而不是默认的-。如 果将符号说明符指定为空格，会在正数前面加上空格而不是+
print('{0:-.2}\n{1:-.2}'.format(pi, -pi))
print('{0:+.2}\n{1:+.2}'.format(pi, -pi))
print('{0: .2}\n{1: .2}'.format(pi, -pi))

#需要介绍的最后一个要素是井号(#)选项，你可将其放在符号说明符和宽度之间(如果指 定了这两种设置)。这个选项将触发另一种转换方式，转换细节随类型而异
#例如，对于二进制、 八进制和十六进制转换，将加上一个前缀。
print("{:b}".format(42))
print("{:#b}".format(42))

#对于各种十进制数，它要求必须包含小数点(对于类型g，它保留小数点后面的零)
print("{:g}".format(42))
print("{:#g}".format(42))
```
- 以下代码分两次设置字符串格式，其中第一次旨在插入最终将作为格式说明符的字段宽度。因为这些信息是用户输入的，无法以编码方式指定字符宽度：
```python
#根据指定的宽度打印格式良好的价格列表（键入的值要大一些）
width = int(input('Please enter width: '))

price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt        = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('=' * width)

print(header_fmt.format('Item', 'Price'))

print('-' * width)

print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))

print('=' * width)
```

## 字符串方法 ##
前面介绍了列表的方法，而字符串的方法要多得多，因为其很多方法都是从模块string那里 “继承”而来的。
字符串的方法太多了，这里只介绍一些最有用的。

### 模块String 未死 ###
虽然字符串方法完全盖住了模块string的风头，但这个模块包含一些字符串没有的常量 和函数。
```下面就是模块string中几个很有用的常量```
|常量|描述|
|:-|:-|
|string.digits|包含数字0~9的字符串|
|string.ascii_letters|包含所有ASCII字母(大写和小写)的字符串|
| string.ascii_lowercase|包含所有小写ASCII字母的字符串|
|string.printable|包含所有可打印的ASCII字符的字符串|
| string.punctuation|包含所有ASCII标点字符的字符串|
|string.ascii_uppercase|包含所有大写ASCII字母的字符串|
虽然说的是ASCII字符，但值实际上是未解码的Unicode字符串

### center（居中） ###
```python
#通过两边填充字符（默认为空格）让字符串居中
print("The Middle by Jimmy Eat World".center(39))
#通过两边填充字符（使用“*”）让字符串居中
print("The Middle by Jimmy Eat World".center(39, "*"))
```
### find（在字符串中查找子串，找到就返回索引，找不到就是-1） ###
```python
#方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。
print('With a moo-moo here, and a moo-moo there'.find('moo'))
title = "Monty Python's Flying Circus"
print(title.find('Monty'))
print(title.find('Python'))
print(title.find('Flying'))
print(title.find('Zirquss'))
subject = '$$$ Get rich now!!! $$$'
print(subject.find('$$$'))

#字符串方法find返回的并非布尔值。如果find像这样返回0，就意味着它在索引0处找到 了指定的子串。
#指定搜索的起点和终点(它们都是可选的)。
subject = '$$$ Get rich now!!! $$$'
print(subject.find('$$$'))
# 只指定了起点
print(subject.find('$$$', 1))
print(subject.find('!!!'))
# 同时指定了起点和终点
print(subject.find('!!!', 0, 16))
```
### join（合并序列元素） ###
```python
#join作用与split相反，用于合并序列的元素
seq = [1, 2, 3, 4, 5]
sep = '+'
# 尝试合并一个数字列表（报错啦，类型不匹配）
# print(sep.join(seq))
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# TypeError: sequence item 0: expected string, int found
seq = ['1', '2', '3', '4', '5']
#合并一个字符串列表
print(sep.join(seq))
dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))
print('C:' + '\\'.join(dirs))
```

### lower（字符串小写） ###
```python
#方法lower返回字符串的小写版本。
print('Trondheim Hammer Dance'.lower())
#当在判断一个字符是否在某一个数组中时，我们不忽略大小写就会无法找到，如下，是不会打印出"Found it!"的
if 'Gumby' in ['gumby', 'smith', 'jones']: print('Found it!')
#那我们怎么做呢，看下面
name = 'Gumby'
names = ['gumby', 'smith', 'jones']
if name.lower() in names: print('Found it!')
```

### replace（指定子串都替换为另一个字符串） ###
```python
#将is替换成eez
print('This is a test'.replace('is', 'eez'))
```

### split（其作用与join相反，用于将字符串拆分为序列）  ###
```python
#将字符串以"+"分隔成数组
print('1+2+3+4+5'.split('+'))
#将字符串以"/"分隔成数组
print('/usr/bin/env'.split('/'))
#如果没有指定分隔符，将默认在单个或多个连续的空白字符(空格、制表符、换行符 等)处进行拆分。
print('Using the default'.split())
```

### strip（删除空字符串） ###
```python
print(' internal whitespace is kept '.strip())
#定用户输入用户名时不小心在末尾加上了一个空格
names = ['gumby', 'smith', 'jones']
name = 'gumby '
#下面是没有'Found it!'的
if name in names: print('Found it!')
#去空格就会出现了
if name.strip() in names: print('Found it!')
#在一个字符串参数中指定要删除哪些字符
print('*** SPAM * for * everyone!!! ***'.strip(' *!'))
```
### translate ###
方法translate与replace一样替换字符串的特定部分，但不同的是它只能进行单字符替换。 这个方法的优势在于能够同时替换多个字符，因此效率比replace高。
这个方法的用途很多(如替换换行符或其他随平台而异的特殊字符)，但这里只介绍一个比 较简单(也有点傻)的示例。假设你要将一段英语文本转换为带有德国口音的版本，为此必须将 字符c和s分别替换为k和z。
然而，使用translate前必须创建一个转换表。这个转换表指出了不同Unicode码点之间的转 换关系。要创建转换表，可对字符串类型str调用方法maketrans，这个方法接受两个参数:两个 长度相同的字符串，它们指定要将第一个字符串中的每个字符都替换为第二个字符串中的相应字 符1。就这个简单的示例而言，代码类似于下面这样。
```python
table = str.maketrans('cs', 'kz')
print(table)
#创建转换表后，就可将其用作方法translate的参数。
print('this is an incredible test'.translate(table))
#调用方法maketrans时，还可提供可选的第三个参数，指定要将哪些字母删除。例如，要模 仿语速极快的德国口音，可将所有的空格都删除。
table = str.maketrans('cs', 'kz', ' ')
print('this is an incredible test'.translate(table))
```

### 判断字符串是否满足特定的条件 ###
- isalnum
- isalpha
- isdecimal
- isdigit
- isidentifier
- islower
- isnumeric
- isprintable
- isspace
- istitle
- isupper

## GitHub 代码 ##
[GItHub Address](https://github.com/FrankCy/FrankPython/tree/master/FP-3)

