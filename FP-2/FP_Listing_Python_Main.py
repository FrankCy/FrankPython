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


############### 基本的列表操作 ###############
# 1. append
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