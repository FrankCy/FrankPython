# FP-2 第二章内容练习 #

- F{_Array.py
数组语法练习

- FP_Listing_Python_Main.py
列表:Python主力

- FP_Tuple.py
元组（不可修改的序列）


## 简介 ##
Python内置了多种元组，这里重点介绍其中最常用两种：```列表```、```元组```。
让我们先来认识一下列表，常规🌰，如下
- 假定查询关系型数据（返回条目信息，并放入一个```列表```中）:
```
#定义基础数组
edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
database = [edward, john]
#将列表转换成String，输出
print('数组为:'+database.__str__())
```

- 知识点
Python有一种数据结构的基本概念，名为容器(container)。所谓容器，就是装东西的，可以包含好多好多对象，对象包含对象啥的。```两种主要的容器是序列(如列表和元组)和映射(如字典)，序列中，每个元素都是编号，而在映射中每个元素都有名称（键）```—— [Python 映射]()。```有一种既不是序列也不是映射的容器，它就是集合【Set】```。

## 通用序列操作 ##
有几种操作适合所有序列，例如```索引、切片、相加、相乘```和```成员资格```检查。
### 索引 ###
所有的元素都有编号，```从0```开始！
```
#数组索引
greeting = 'Hello'
print(greeting[0])

#负数索引（从右至左）
print(greeting[-1])

#输入一个数，并打印索引3的值
fourth = input('Year: ')[3]
print(fourth)
```

### 切片 ###

```

############### 切片 ###############
#切片访问字符（截取字符串）
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[32:-4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[0:1])
print(numbers[7:10])

#负数索引-切片（依然从右至左）
print(numbers[-3:-1])
# print(numbers[-3:0]) #这句话无效，倒数第三个数在第一个数前面，错误语法

#还可以这么写
print(numbers[-3:])

#还可以这么写2
print(numbers[:3])

#使用所有序列的写法
print(numbers[:])

#获取第12个字符到倒数第4个字符
# url = input('Please enter the URL:')
# domain = url[11:-4]
# print("Domain name: " + domain)

#另一种写法：指定分片步长（1），意思是取0——10，但以1为步长获取
print(numbers[0:10:1])

#取0——10，但以2为步长获取
print(numbers[0:10:2])

#取3——6，但以3为步长获取
print(numbers[3:6:3])

#另一种写法：每隔3个获取1个数
print(numbers[::4])

#注：步长不能为0，否则不能向前移动，也没有意义，但是可以为负数
print(numbers[8:3:-1])
print(numbers[10:0:-2])
print(numbers[0:10:-2])
print(numbers[::-2])
print(numbers[5::-2])
print(numbers[:5:-2])
```

### 序列相加 ###
```
############### 序列相加 ###############
#使用加法运算符来拼接序列
print([1, 2, 3] + [4, 5, 6])
print('Hello,' + 'world!')
# 以下这行会错误，无法将列表和字符串进行拼接
# print([1, 2, 3] + 'world!')
# Traceback (innermost last):
# File "<pyshell>", line 1, in ? [1, 2, 3] + 'world!'
# TypeError: can only concatenate list (not "string") to list
```

### 乘法 ###
```
############### 乘法 ###############
print('python' * 5)
print([42] * 10)

# None、空列表和初始化
# Python中 "None"表示什么也没有，我们如何创建10个什么也没有的参数呢，下面创建一个什么也没有长度为10的列表
sequence = [None] * 10
print(sequence)

#在屏幕中显示一行话
sentence = input("Sentence: ")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)
print()
print(' ' * left_margin + '+' + '-' * (box_width - 2) +  '+')
print(' ' * left_margin + '|' + ' ' * text_width      + ' |')
print(' ' * left_margin + '|' +       sentence        + ' |')
print(' ' * left_margin + '|' + ' ' * text_width      + ' |')
print(' ' * left_margin + '+' + '-' * (box_width - 2) +  '+')
print()
```
### 成员资格 ###
```
############### 成员资格###############
#判断
permissions = 'rw'
print('w' in permissions)
print('x' in permissions)

users = ['mlh', 'foo', 'bar']
#输入一个参数，判断是否包含在列表内
# input('Enter your user name: ') in users

subject = '$$$ Get rich now!!! $$$'
print('$$$' in subject)

# 检查用户名和PIN码
# database = [
#     ['albert', '1234'],
#     ['dilbert', '4242'],
#     ['smith', '7524'],
#     ['jones', '9843']
# ]
#
# username = input('User name: ')
# pin = input('PIN code: ')
# if [username, pin] in database :print('Access granted')

#获取列表中长度及大小
numbers = [100, 34, 678]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(max(2, 3))
print(min(9, 3, 2, 5))
```

## 列表 （Python主力） ##
列表有很多特有的方法
### 函数list ###
```list实际上是一个类，而不是函数，但眼下，这种差别并不重要```
```
############### list ###############
somelist=list('Hello')
#输出字符列表
print(somelist)
#字符列表转换成字符串
print(''.join(somelist))
```

### 基本的列表操作 ###
```
############### 基本的列表操作 ###############
#修改列表，给元素赋值
x = [1, 1, 1]
x[1] = 2
print(x)

#删除元素
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)

#给切片赋值
name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)

#给多个元素赋值
name = list('Perl')
name[1:] = list('ython')
print(name)

#替换值
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)

#替换值（替换成'什么也没有'）
numbers[1:4] = []
print(numbers)
```

### 列表方法 ###

定义：方法是与对象(列表、数、字符串等)联系紧密的函数
表现形式：```object.method(arguments)```
```
# 2.3 列表:Python主力


############### list ###############
somelist=list('Hello')
#输出字符列表
print(somelist)
#字符列表转换成字符串
print(''.join(somelist))


############### 基本的列表操作 ###############
#修改列表，给元素赋值
x = [1, 1, 1]
x[1] = 2
print(x)

#删除元素
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)

#给切片赋值
name = list('Perl')
print(name)
name[2:] = list('ar')
print(name)

#给多个元素赋值
name = list('Perl')
name[1:] = list('ython')
print(name)

#替换值
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)

#替换值（替换成'什么也没有'）
numbers[1:4] = []
print(numbers)


############### 列表方法 ###############
- 1. append
lst = [1, 2, 3]
lst.append(4)
print(lst)

# 2. clear
lst = [1, 2, 3]
lst.clear()
print(lst)

# 3. copy
a = [1, 2, 3]
b = a
b[1] = 4
print(a)
# 要让a和b指向不同的列表，就必须将b关联到a的副本,如下：
a = [1, 2, 3]
b = a.copy()
b[1] = 4
print(a)
# 这类似于使用a[:]或list(a)，它们也都复制a。

# 4. count
#方法count计算指定的元素在列表中出现了多少次。
print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))
print(x.count([1, 2]))

# 5. extend（继承）
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
#正常使用
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
print(a)

# 6. index
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))

# print(knights.index('herring')) #这句话会报错，因为没有herring
# Traceback (innermost last):
# File "<pyshell>", line 1, in ?
# knights.index('herring')
# ValueError: list.index(x): x not in list

#搜索单词'who'时，发现它位于索引4处。
print(knights[4])

# 7. insert
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print(numbers)

numbers = [1, 2, 3, 5, 6, 7]
numbers[3:3] = ['four']
print(numbers)

# 8. pop
#方法pop从列表中删除一个元素(末尾为最后一个元素)，并返回这一元素。
x = [1, 2, 3]
print(x.pop())
print(x)
print(x.pop(0))
print(x)
#pop是唯一既修改列表又返回一个非None值的列表方法。
# **** 使用pop可实现一种常见的数据结构——栈(stack)。栈就像一叠盘子，你可在上面添加盘子， 还可从上面取走盘子。最后加入的盘子最先取走，这被为后进先出(LIFO)。 ***

#pop作为取出一个元素，对应的应该还有加入一个元素，但是Python没有push，我们可以用append替代
x = [1, 2, 3]
x.append(x.pop())
print(x) #结果相同，因为我们取走了末尾的3，又增加了一个末尾的3，程序执行好比 1,2,3 + 3（x.append()) 1，2，3-3 （x.pop)

# 9. remove
#方法remove用于删除第一个为指定值的元素。
x = ['to', 'be', 'or', 'not', 'to', 'be']
print(x.remove('be'))
# print(x.remove('bee'))
# Traceback (innermost last):
# File "<pyshell>", line 1, in ? x.remove('bee')
# ValueError: list.remove(x): x not in list

# 10. reverse
#方法reverse倒排元素。
x = [1, 2, 3]
print(x.reverse())
print(list(reversed(x)))

# 11. sort
x = [4, 6, 2, 1, 7, 9]
print(x.sort())

#鉴于sort修改x且不返回任何值，最终的结果是x是经过排序的，而y包含None:
x = [4, 6, 2, 1, 7, 9]
y = x.sort()
print(y)
#为实现前述 目标，正确的方式之一是先将y关联到x的副本，再对y进行排序，如下所示：
x = [4, 6, 2, 1, 7, 9]
y = x.copy()
y.sort()
print(x)
print(y)

#只是将x赋给y是不可行的，因为这样x和y将指向同一个列表。
#为获取排序后的列表的副本， 另一种方式是使用函数sorted:
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print(y)
print(x)

#实际上，这个函数可用于任何序列，但总是返回一个列表
print(sorted('Python'))

#如果要将元素按相反的顺序排列，可先使用sort(或sorted)，再调用方法reverse，也可使用参数reverse，这将在下一小节介绍。

# 12. 高级排序
#方法sort接受两个可选参数:key和reverse。这两个参数通常是按名称指定的，称为关键字 参数，将在第6章详细讨论。参数key类似于参数cmp:你将其设置为一个用于排序的函数。然而， 不会直接使用这个函数来判断一个元素是否比另一个元素小，而是使用它来为每个元素创建一个 键，再根据这些键对元素进行排序。因此，要根据长度对元素进行排序，可将参数key设置为函数len。
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print(x)
#对于另一个关键字参数reverse，只需将其指定为一个真值(True或False，将在第5章详细介 绍)，以指出是否要按相反的顺序对列表进行排序。
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)
```

## 元组:不可修改的序列 ##
与列表一样，元组也是序列，唯一的差别在于元组是```不能修改```的(你可能注意到了，字符串 也不能修改)。元组语法很简单，只要将一些值用逗号分隔，就能自动创建一个元组。

### 例举元组 ###
```
############## 例举元组 ##############
print((1, 2, 3))
#空元组 （）

#通过函数tuple将序列转换成元组
print(tuple([1, 2, 3]))
print(tuple('abc'))
print(tuple((1, 2, 3)))
```
```元组的切片也是元组，就像列表的切片也是列表一样```,为何要熟悉元组呢?原因有以下两个：
- 它们用作映射中的键(以及集合的成员)，而列表不行
- 有些内置函数和方法返回元组，这意味着必须跟它们打交道。只要不尝试修改元组，与元组“打交道”通常意味着像处理列表一样处理它们(需要使用元组没有的index和count 10 等方法时例外)。


##  总结 ##
- 序列
序列是一种数据结构，其中的元素带编号(编号从0开始)。列表、字符串和元组
都属于序列，其中列表是可变的(你可修改其内容)，而元组和字符串是不可变的(一旦 创建，内容就是固定的)。要访问序列的一部分，可使用切片操作:提供两个指定切片起 始和结束位置的索引。要修改列表，可给其元素赋值，也可使用赋值语句给切片赋值。

- 成员资格
要确定特定的值是否包含在序列(或其他容器)中，可使用运算符in。将运 算符in用于字符串时情况比较特殊——这样可查找子串。

- 方法
一些内置类型(如列表和字符串，但不包括元组)提供了很多有用的方法。方法 有点像函数，只是与特定的值相关联。方法是面向对象编程的一个重要方面，这将在第7 章介绍。

## 以上出现过的函数 ##
| 函数 | 描述 |
|:--|:--|
| len(seq) | 返回序列的长度 |
| list(seq) | 将序列转换为列表 |
| max(args) | 返回序列或一组参数中的最大值 |
| min(args) | 返回序列和一组参数中的最小值 |
| reversed(seq) | 让你能够反向迭代序列 |
| sorted(seq) | 返回一个有序列表，其中包含指定序列中的所有元素 |
| tuple(seq) | 将序列转换为元组 |