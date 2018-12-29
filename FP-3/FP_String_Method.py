######## 字符串方法 ########
### center ###
#通过两边填充字符（默认为空格）让字符串居中
print("The Middle by Jimmy Eat World".center(39))
#通过两边填充字符（使用“*”）让字符串居中
print("The Middle by Jimmy Eat World".center(39, "*"))

### find ###
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


### join ###
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

### lower（字符串小写） ###
#方法lower返回字符串的小写版本。
print('Trondheim Hammer Dance'.lower())
#当在判断一个字符是否在某一个数组中时，我们不忽略大小写就会无法找到，如下，是不会打印出"Found it!"的
if 'Gumby' in ['gumby', 'smith', 'jones']: print('Found it!')
#那我们怎么做呢，看下面
name = 'Gumby'
names = ['gumby', 'smith', 'jones']
if name.lower() in names: print('Found it!')


### replace（指定子串都替换为另一个字符串） ###
#将is替换成eez
print('This is a test'.replace('is', 'eez'))


### split（其作用与join相反，用于将字符串拆分为序列） ###
#将字符串以"+"分隔成数组
print('1+2+3+4+5'.split('+'))
#将字符串以"/"分隔成数组
print('/usr/bin/env'.split('/'))
#如果没有指定分隔符，将默认在单个或多个连续的空白字符(空格、制表符、换行符 等)处进行拆分。
print('Using the default'.split())

### strip（删除空字符串） ###
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

### translate ###
table = str.maketrans('cs', 'kz')
print(table)
#创建转换表后，就可将其用作方法translate的参数。
print('this is an incredible test'.translate(table))
#调用方法maketrans时，还可提供可选的第三个参数，指定要将哪些字母删除。例如，要模 仿语速极快的德国口音，可将所有的空格都删除。
table = str.maketrans('cs', 'kz', ' ')
print('this is an incredible test'.translate(table))


### 判断字符串是否满足特定的条件 ###
#附录B:isalnum、isalpha、isdecimal、isdigit、isidentifier、islower、isnumeric、 isprintable、isspace、istitle、isupper

