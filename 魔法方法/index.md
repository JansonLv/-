![](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp15Ygj7AUy9icHU8MlMh8icAy2vTCWicoEZVl0ibgVFDZg4GzVYwMaCNoV2wAnSPKYYrwWJbW9aqDAribg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/qX7rSBgoEp15Ygj7AUy9icHU8MlMh8icAyWwOiaSZd4ByicKPEcMn6AZEBNIlfulOYxy2bFtylHhmDYt63ejkwiasRg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## __ __repr__ __
Python中这个__repr__函数，对应repr(object)这个函数，返回一个可以用来表示对象的可打印字符串.
如果我们直接打印一个类，像下面这样
```python
class A():
    def __init__(self,name=None,id=1):
        self.id=id
        self.name=name

if __name__ == '__main__':
    a=A()
    print(a)
```
输出结果
```
<__main__.A object at 0x0000018DF8E7EAC8>
```
不是很友好，返回了一个对象的内存地址。
我们改成下面再次输出
```python
class A():
    def __init__(self,name=None,id=1):
        self.id=id
        self.name=name
    def __repr__(self):
        return "进入函数"

if __name__ == '__main__':
    print(A())
```
输出
```
进入函数
```
## __ __str__ __
```python
class A():
    def __init__(self,name=None,id=1):
        self.id=id
        self.name=name
    def __str__(self):
        return "进入函数"

if __name__ == '__main__':
    print(A())
```
输出结果
```
进入函数
```

#### 比较repr和str
```
上面我们发现在print的时候，两个魔法函数显示的效果是一样的，那这两个魔法函数区别在哪呢，__repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员。在print的时候两者项目一样，但是在交互命令下
__repr__同样有着print的效果，但是__str__还是输出对象内存地址。也就说在交互式命令下我们可以看到其效果，另外__str__ 方法其实调用了 __repr__ 方法。
```


## __ __getitem__ __
如果在类中定义了getitem__()方法，那么他的实例对象（假设为A）就可以这样A[key]取值。当实例对象做A[key]运算时，就会调用类中的__getitem()方法。
```python
class A():
    def __init__(self,name=None,id=1):
        self.id=id
        self.name=name
    def __repr__(self):
        return "进入函数"
    def __getitem__(self, item):
       return item

if __name__ == '__main__':
    a=A('lisa','123')
    print(a['name'])
    print(a[124])
```
输出
```
name
124
```
实例对象的key不管是否存在都会调用类中的__getitem__()方法。而且返回值就是__getitem__()方法中规定的return值。也就是说如果getitem里的方法写的不好就没有了意义了。
我们修改下代码，改变getitem的return的值
```python {.line-numbers}
class A():
    def __init__(self,name=None,id=1):
        self.id=id
        self.name=name
    def __repr__(self):
        return "进入函数"
    def __getitem__(self, item):
       return self.__dict__[item]

if __name__ == '__main__':
    a=A('lisa','123')
    print(a['name'])
    print(a[123])
```
输出
```
lisa
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "<stdin>", line 8, in __getitem__
KeyError: 123
```
输出了lisa和一个异常，改后的getitem做了什么事呢，
self.__dict__,是获取当前实例的所有属性的字典格式，后面的[item]就是取其对于的键值，这里我传了个name,实际就是取name属性的值也就是lisa。
对于123因为不存在这个属性所有报错了。这也是字典内部实现的一部分。

再来看一个例子,代码里已经加入了注释:
```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

# 具名元组动态创建一个类Card，并含有两个属性rank和suit
# 用以构建只有少数属性但是没有方法的对象

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 扑克牌2到A组成的列表
    suits = 'spades diamonds clubs hearts'.split()  # 四种花色

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]  # 笛卡尔积，13*4=52(除去两个王)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # 调用f[0]时会进入
        return self._cards[position]


if __name__ == '__main__':
    f = FrenchDeck()

    print(f[0])
    # 在这里f[0]实际是f.__getitem__(0)
```
输出
```
Card(rank='2', suit='spades')
```
因为Card是一个具名元祖创建的动态类，所以显示rank='2', suit='spades'该格式。
我们发现这个例子中还有一个__len__,那这个方法是干嘛的呢，我们继续往下看

### __ __len__ __
在上面的例子中我们使用该方法，这个方法会在什么情况下发生呢，一个小例子来说明。
```python
class B():

    def __init__(self):
        self.a_list = range(10)

    def __len__(self):
        return len(self.a_list)


if __name__ == '__main__':
     b = B()
     print(len(b))
     #在这里等价于
     #print(b.__len__())
```
输出
```
10
```
我们在调用len方法的时候会调用__len__。

### __ __setitem__ __
__ __setitem__ __(self,key,value)：该方法应该按一定的方式存储和key相关的value。在设置类实例属性时自动调用的。
```python
class B():

    def __init__(self):
        self.a_list = range(10)

    def __setitem__(self, key, value):
        self.__dict__[key] = value


def cfun(a, b, c):
    a.__dict__[b] = c
    print(f"新增key:{b}, value:{c}")


if __name__ == '__main__':
    b = B()
    b['a_list'] = "123"  # 这个会调用B类的__setitem__方法
    print(b.a_list)
    B.__setitem__ = cfun  # 改变settime方式变为cfun这个函数
    b['b_list'] = "123"  # 这次实际会调用cfun函数
    print(b.b_list)
```
输出
```
123
新增key:b_list, value:123
123
```
### __ __delitem__ __

执行del函数的时候会调用，如果继承了 继承
abc.MutableSequence的类就必须实现 __delitem__ 方法，这是 MutableSequence 类的一个抽象方法。

定义删除容器中指定元素的行为，相当于
```python
del self[key]
```

### __ __eq__ __
a == b等同于a.__eq__(b)。
你可以在自己的类中定义 __eq__ 方法，决定 == 如何比较
实例。如果不覆盖 __eq__ 方法，那么从 object 继承的方法比较


