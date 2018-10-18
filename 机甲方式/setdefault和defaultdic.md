## setdefault
顾名思义就是设置默认值，不过设置之前会多一次get,如果key存在值取value，不存在则设置

```python
data = {"aa": 22}
print(data.setdefault("aa", 33))
print(data)

print(data.setdefault("bb", 33))
print(data)

'''Output
22
{'aa': 22}
33
{'aa': 22, 'bb': 33}
'''

```

## defaultdict

defaultdict是属于collections 模块下的一个工厂函数，用于构建字典对象，接收一个函数（可调用）对象为作为参数。参数返回的类型是什么，key对应value就是什么类型。

    >>> result = defaultdict(list)

    >>> result

    defaultdict(<type 'list'>, {})

    >>> result['a']

    []

#### 示例
```python
data = [("p", 1), ("p", 2), ("p", 3),

        ("h", 1), ("h", 2), ("h", 3)]

#要转换成
result = {'p': [1, 2, 3], 'h': [1, 2, 3]}

# 使用setdefault
for (key, value) in data:
    result.setdefault(key, []).append(value)
    
# 使用defaultdict
result = defaultdict(list)
for (key, value) in data:
    result[key].append(value)
```


