## map函数

map(function_object, iterable1, iterable2, ...)

map函数需要一个函数对象和任意数量的iterables，如list、dictionary等。它为序列中的每个元素执行function_object，并返回由函数对象修改的元素组成的列表。

#### 示例如下：
```python {.line-numbers}
# python3
add = lambda x: x+2

x = map(add, [1,2,3,4,5])
print(x)  # OutPut:<map object at 0x1078486a0>
# 实例化一个map对象,或者说一个迭代器

# 增加list变成一个列表
x = list(map(add, [1,2,3,4,5]))
print(x)  # Output:[3, 4, 5, 6, 7]

# 通过for循环迭代遍历
for i in map(add, [1,2,3,4,5]):
    print(i)
```

```
Python 2.7.15 |Anaconda, Inc.| (default, May  1 2018, 18:37:05) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> add = lambda x: x+2
>>> 
>>> x = map(add, [1,2,3,4,5])
>>> print(x) 
[3, 4, 5, 6, 7]
```

-python2 map出来的是数组
在Python3中，map函数返回一个惰性计算（lazily evaluated）的迭代器（Iterator）或map对象。就像zip函数是惰性计算那样。_



