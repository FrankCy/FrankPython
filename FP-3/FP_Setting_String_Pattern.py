######## 设置字符串的格式:完整版 ########
print("{{ceci n'est pas une replacement field}}".format())
#format可传递3个参数，每个参数都是可选的

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

######## 宽度、精度和千位分隔符 ########
pi = 3.14
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

######## 符号、对齐和用0填充 ########
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

#以下代码分两次设置字符串格式，其中第一次旨在插入最终将作为格式说明符的字段宽度。因为这些信息是用户输入的，无法以编码方式指定字符宽度：
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



