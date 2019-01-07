######## 字典 ########
#获取电话薄Cecil的电话
#print(phonebook["Cecil"])

#定义电话薄
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(phonebook["Cecil"])

#将满足键值结构值转换为字典
#定义items
items = [('name', 'Gumby'), ('age', 42)]

#调用dict转换，通过items创建字典d
d = dict(items)
print(d)
print(d.get("name"))

#通过关键字实参
d = dict(name = 'Join', age = 55)
print(d)
print(d.get("name"))

#列表与字典在声明对象时的区别
# x = []
# x[42] = "阿里巴巴"
# print(x[42])
# Traceback (most recent call last):
# File "<stdin>", line 1, in ?
# IndexError: list assignment index out of range
# 上面会报错，因为列表中如果想指定42是阿里巴巴，就需要先创建 x = [None] * 43类似的的代码，才允许使用。
x = {}
x[42] = "阿里巴巴"
print(x)
# 反观字典，是不会出现这种错误的

# 根据入参，判断字典中的数据，并获得想要的数据（类似查询一个数据库，然后把值放到字典中，前端调用）
people = {
    'Alice' : {
        'phone' : '2341',
        'addr' : 'Foo drive 23'
    },

    'Beth' : {
        'phone' : '9102',
        'addr' : 'Bar street 42'
    },

    'Cecil' : {
        'phone' : '3158',
        'addr' : 'Bar street 42'
    }
}

# 电话号码和地址的描述标签，供打印输出时使用
# labels = {
#     'phone' : 'phone number',
#     'addr' : 'address'
# }
#
# name = input('Name : ')
#
# # 查找的是电话还是地址
# request = input('Phone number (p) or address (a)?')
#
# # 使用正确的键
# if request == 'p' : key = 'phone'
# if request == 'a' : key = 'addr'
#
# # 仅当名字是字典包含的键时才打印信息
# if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

# 动态赋值，从phonebook中找到Cecil，并动态放入输出语句中
print("Cecil's phone number is {Cecil}.".format_map(phonebook))

# 将转换说明符应用到动态页面当中
template = '''
<html>
    <head>
        <title>{title}</title>
        <body>
            <h1>{title}</h1>
            <p>{text}</p>
        </body>
    </head>
</html>
'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template.format_map(data))

### 字典方法 ###
# clear
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)

returned_value = d.clear();
print(d)
print(returned_value)

# copy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy();
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)

# 深复制deecopy
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

# fromkeys
print({}.fromkeys(['name', 'age']))
# 另一种写法，通过dict（所有字典所属类型）进行创建
print(dict.fromkeys(['name', 'age']))
# 直接赋值
print(dict.fromkeys(['name', 'age'], '我是默认值'))

# get
# 模拟一个数据库操作
# labels = {
#     'phone' : 'phone number',
#     'addr' : 'address'
# }
#
# name = input("Name: ")
#
# request = input('Phone number (p) or address (a)? ')
# # 如果request既不是'p'也不是'a' if request == 'p': key = 'phone'
# key = request
# if request == 'a': key = 'addr'
# # 使用get提供默认值
# person = people.get(name, {})
# label = labels.get(key, key)
# result = person.get(key, 'not available')
# print("{}'s {} is {}.".format(name, label, result))

# items
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())

# 赋值
it = d.items()
# 获取字典有多少个项
print(len(it))
# 判断项spam是不是等于0
print(('spam', 0) in it)

# pop
d = {'x' : 1 , 'y' : 2}
print(d.pop('x'))
print(d)

# popitem
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print(d.popitem())
print(d)

# setdefault
d = {}
print(d.setdefault('name', 'N/A'))
print(d)
d['name'] = 'Gumby'
print(d.setdefault('name', 'N/A'))
print(d)
d = {}
print(d.setdefault('name'))
print(d)

# update
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
}
print(d)
# 设置一个新的title
x = {'title': 'Python Language Website'}
# 将原title修改
d.update(x)
print(d)

# values
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print(d.values())