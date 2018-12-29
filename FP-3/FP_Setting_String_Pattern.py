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

