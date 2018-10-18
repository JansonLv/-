## filter过滤

##### filter的基本语法如下：

    filter(function_object, iterable)

filter函数需要两个参数，function_object返回一个布尔值（boolean），对iterable的每一个元素调用function_object，filter只返回满足function_object为True的元素。

和map函数一样，filter函数也返回一个list，但与map函数不同的是，filter函数只能有一个iterable作为输入。

##### 示例
```python
a = [1, 2, 3, 4, 5, 6]

list[filter(lambda x : x % 2 == 0, a)]

# Output: [2, 4, 6]
```
和map的问题是一样的，python3中返回一个可迭代对象，python2中返回一个列表

