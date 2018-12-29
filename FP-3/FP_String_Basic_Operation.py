######## 字符串基本操作 ########
website = 'http://www.python.org'
website[-3:] = 'com'
# Traceback (most recent call last):
#        File "<pyshell#19>", line 1, in ?
# website[-3:] = 'com'
# TypeError: object doesn't support slice assignment
# 字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的，上面代码是错误的！