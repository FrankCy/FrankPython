# 2.2 通用序列操作

#定义基础数组
edward = ['Edward Gumby', 42]
john = ['John Smith', 50]
database = [edward, john]
print('数组为:'+database.__str__())

#数组索引
greeting = 'Hello'
print(greeting[0])

#负数索引（从右至左）
print(greeting[-1])

#输入一个数，并打印索引3的值
#fourth = input('Year: ')[3]
#print(fourth)

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

############### 序列相加 ###############
#使用加法运算符来拼接序列
print([1, 2, 3] + [4, 5, 6])
print('Hello,' + 'world!')
# 以下这行会错误，无法将列表和字符串进行拼接
# print([1, 2, 3] + 'world!')
# Traceback (innermost last):
# File "<pyshell>", line 1, in ? [1, 2, 3] + 'world!'
# TypeError: can only concatenate list (not "string") to list

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

############### 成员资格 ###############
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