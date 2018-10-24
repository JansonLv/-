## 便利库

#### ChainMap

ChainMap是由Python标准库提供的一种数据结构，允许你将多个字典视为一个。

ChainMap上的官方文档如下：

ChainMap将多个dict或其他映射组合在一起以创建单个可更新视图。[…] 查找基础映射，直到找到key为止。[…]如果其中一个基础映射得到更新，这些更改将反映在ChainMap中。 […] 支持所有常用的字典方法。

换句话说:ChainMap是一个基于多dict的可更新的视图，它的行为就像一个普通的dict。

你以前可能从来没有听说过ChainMap，你可能会认为ChainMap的使用情况是非常特定的。坦率地说，你是对的。

我知道的用例包括：
- 通过多个字典搜索
- 提供链缺省值(和dict.get一样)
- 经常计算字典子集的性能关键的应用程序

我们将通过例子来说明。

```python
toys = {'blocks': 30, 'monkey': 20}

computer = {"lianxiang": 3000, "macbook": 10000}

from collections import ChainMap

things = ChainMap(toys, computer)
print(things["macbook"])
print(things)
# 输出
# 10000
# ChainMap({'blocks': 30, 'monkey': 20}, {'lianxiang': 3000, 'macbook': 10000})
print(things.pop("monkey"))
# 20
print(things.pop("lianxiang"))
# "Key not found in the first mapping: 'macbook'"   由此可见，只能pop第一个穿进去的dict
```

应用场景：配置文件