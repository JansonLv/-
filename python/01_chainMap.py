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
