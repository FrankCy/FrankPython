#单引号
print('Hello, world!')
#双引号
print("Hello, world!")
#字符串拼接
print("\"Hello, world!\" she said")
#单引号括双引号，输出与字符串拼接一致
print('"Hello, world!" she said')

#字符拼接，包含单引号，repr是一个函数
print(repr("Hello,\nworld!"))

#字符拼接，包含单引号，str是一个会把\n认为是一个换行符
print(str("Hello,\nworld!"))

#大字符串表示 使用三引号 '''
print('''This is a very long string. It continues here. And it's not over yet. "Hello, world!" Still here.''')

#大字符串表示 使用三双引号 """ xxxx """
print("""This is a very long string. It continues here. And it's not over yet. "Hello, world!" Still here.""")

#输出盘符，因为盘符包含"\"，识别的时候会有问题
print("c:\abc.py")
print("c:\\abc.py")
#r的作用
print(r"c:\abc.py")
print(r'C:\Program Files\foo\bar' '\\')

#输出Unicode
print("\u00C6")
print("\U0001F60A")
print("This is a cat: \N{Cat}")

#转码
print("Hello, world!".encode("ASCII"))
print("Hello, world!".encode("UTF-8"))
print("Hello, world!".encode("UTF-32"))
#转码长度
print(len("How long is this?".encode("UTF-8")))
print(len("How long is this?".encode("UTF-32")))

# print("Hællå, wørld!".encode("ASCII")) 这行有错误 —— 斯堪的纳维亚字母没有对应的ASCII编码。
print("Hællå, wørld!".encode("ASCII", "ignore"))
print("Hællå, wørld!".encode("ASCII", "replace"))
print("Hællå, wørld!".encode("ASCII", "backslashreplace"))
print("Hællå, wørld!".encode("ASCII", "xmlcharrefreplace"))
print("Hællå, wørld!".encode())
print(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!'.decode())
#设置字符编码
print(bytes("Hællå, wørld!", encoding="utf-8"))
print(str(b'H\xc3\xa6ll\xc3\xa5, w\xc3\xb8rld!', encoding="utf-8"))

#bytearray
x = bytearray(b"Hello!")
x[1] = ord(b"u")
x
bytearray(b'Hullo!')

