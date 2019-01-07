# FP-4 档索引行不通时 #

- FB_dictionary.py <br/>
Python字典

# Python 当索引行不通时 #
采用Python的另一数据结构 —— 映射（mapping）。
映射就好比字典，通过Key，去找到对应的Value，好比我要查某个字的意思，我们只需要知道这个字，然后去翻阅我们的字典。
```字典是Python唯一内置映射类型，其中值不按顺序排列，而是存储在键下。键可以是数、字符或元组。```

## 字典的用途 ##
场景：
- 表示棋盘状态，其中每个键都是由坐标组成的元组；
- 存储文件修改时间，其中的键为文件名；
- 数字电话／地址薄；

举例：
例如Java中的Map<K,V>，我们只需创建键值对象，存储时放入值并设置键，获取时直接通过键取到这个对象，如下：
```java
//声明map对象
Map map = new HashMap();
//放入值（放入键为'key'，值为'value'）
map.put("key", "value");
// ...............
//获取key对应的值，并输出（不要在意String.valueOf，这是Java中将对象转换成字符串）
System.out.pritln(String.valueOf(map.get("key")));
```
------------- ```以上是Java的写法```------------
而我们希望在Python中实现类似的操作，例如：
```python
#获取电话薄Cecil的电话
#print(phonebook["Cecil"])
```
在Python中是怎样的语法实现这类操作呢，请看下面。

## 创建和使用字典 ##
首先，我们还是要定义电话薄
```python
#定义电话薄
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
#获取电话薄Cecil的电话，并打印
print(phonebook["Cecil"])
```

Python中的解释如下：
- 字典由```键```及对应```值```组成，这种```键值对象```被称为```项（item）```。
- 示例中，```键```为名字，而```值```为电话号码。```每个键与其值之间都用冒号(:)分隔```，```项```之间用逗号分隔，而整个字典放在花 3 括号内。
- 空字典(没有任何项)用两个花括号表示，类似于下面这样:{}。
- 字典中，键必须是独一无二的，而字典中的值无需如此。

### 函数dict ###
可使用函数dict从其它映射（如其它字典）或键-值对序列创建字典。
```python
#将满足键值结构值转换为字典
#定义items
items = [('name', 'Gumby'), ('age', 42)]

#调用dict转换，通过items创建字典d
d = dict(items)
print(d)
print(d.get("name"))
```
```也可以通过关键字实参调用函数```
```python
#通过关键字实参
d = dict(name = 'Join', age = 55)
print(d)
print(d.get("name"))
```
### 基本的字典操作 ###
字典基本操作：
- len(d)
返回字典d包含的项（键-值对）数。
- d[k]
返回与键k相关联的值。
- d[k] = v
将值v关联到键k。
- del d[k]
删除键为k的项。
- k in a
检查字典d是否包含键为k的项。

字典和列表一些重要的不同之处
- 键的类型
键可以是整数、可以是任何不可变类型，如浮点数（实数）、字符串和元组。
- 自动添加
可以给字典中没有的数值赋值，字典中创建一个新项。不同过append或其它类似方法，就不能给列表中没有的元素赋值。
- 成员资格
表达式k in a，其中a是一个字典，而在列表中，假设x in y ，这里的y是列表。
例子：
```python
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
```
- 例：根据入参，判断字典中的数据，并获得想要的数据（类似查询一个数据库，然后把值放到字典中，前端调用）
```python
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
labels = {
    'phone' : 'phone number',
    'addr' : 'address'
}

name = input('Name : ')

# 查找的是电话还是地址
request = input('Phone number (p) or address (a)?')

# 使用正确的键
if request == 'p' : key = 'phone'
if request == 'a' : key = 'addr'

# 仅当名字是字典包含的键时才打印信息
if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
```

### 将字符串格式设置功能用于字典 ###
```python
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

```

### 字典方法 ###
常用方法
- clear
删除字典项，并没有返回值
```python
# clear
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)

returned_value = d.clear();
print(d)
print(returned_value)
```
- copy
方法copy返回一个新字典，其包含的键值对与原来的字典相同(```这个方法执行的是浅复制， 因为值本身是原件，而非副本```)。
```python
# copy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy();
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)
# y的值
# {'username': 'mlh', 'machines': ['foo', 'baz']}
# x的值
# {'username': 'admin', 'machines': ['foo', 'baz']}
```
经上述x与y的值可以看出，```当替换副本中的值时，原件不受影响。然而，如果修改副本中的值(就地修改而 不是替换)，原件也将发生变化，因为原件指向的也是被修改的值(如这个示例中的'machines' 列表所示)```
为避免这种问题，可执行```深复制(deecopy)```操作
```python
# 深复制deecopy
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc
```
- fromkeys
方法fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None
```python
# 创建一个字典，字典内有2个key，‘name’和‘age’，值为None，用处是声明和赋值使用
print({}.fromkeys(['name', 'age']))

# 另一种写法，通过dict（所有字典所属类型）进行创建
print(dict.fromkeys(['name', 'age']))

# 直接赋值
print(dict.fromkeys(['name', 'age'], '我是默认值'))
```
- get
取值
```python
# 模拟一个数据库操作
labels = {
    'phone' : 'phone number',
    'addr' : 'address'
}

name = input("Name: ")

request = input('Phone number (p) or address (a)? ')
# 如果request既不是'p'也不是'a' if request == 'p': key = 'phone'
key = request
if request == 'a': key = 'addr'
# 使用get提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}.".format(name, label, result))
```
- items
输出字典中所有对象，实际应用可以用来判断字典中是否包含对象或者迭代子
```python
# items
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())

# 赋值
it = d.items()
# 获取字典有多少个项
print(len(it))
# 判断项spam是不是等于0
print(('spam', 0) in it)
```

- keys
方法keys返回一个字典视图，其中包含指定字典中的键。
- pop
方法pop可用于获取与指定键相关联的值，并将该键值对从字典中删除。
```python
# pop
d = {'x' : 1 , 'y' : 2}
print(d.pop('x'))
# 返回1，代表移除了1项
print(d)
# x从d中移除，并生成了一个新的字典，只剩下d
```
- popitem
随机删除字典中的字典项
```python
# popitem
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print(d.popitem())
print(d)
```
- setdefault
与get类似，获取与指定键相关联的值，并且```还在字典不包含指定的键时，在字典中添加指定的键值对```。
```python
# setdefault
# 赋值，当d中无项，会自动增加一个
d = {}
print(d.setdefault('name', 'N/A'))
print(d)
# 赋值并获取
d['name'] = 'Gumby'
print(d.setdefault('name', 'N/A'))
print(d)
# 默认给d一个项，key=name，value=none
d = {}
print(d.setdefault('name'))
print(d)
```
- update
更新项
```python
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
```

- values
方法values返回一个由字典中的值组成的字典视图，返回所有值
```python
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print(d.values())
```

## 总结 ##
- 映射
映射让你能够使用任何不可变的对象(最常用的是字符串和元组)来标识其元素。
Python只有一种内置的映射类型，那就是字典
- 将字符串格式设置功能用于字典
要对字典执行字符串格式设置操作，不能使用format和命名参数，而必须使用format_map。
- 字典方法
字典有很多方法，这些方法的调用方式与列表和字符串的方法相同

## 使用到的新函数 ##
|函数|描述|
|:-|:-|
|dict(seq)|从键-值对、映射或关联字参数创建字典，```一定要符合键值的格式```|