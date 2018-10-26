习惯了高级语言的严谨，总想对属性加以访问控制，相对安全些，比如直接在__init__中定义公用属性，从封装性来说，它是不好的写法。
属性之访问，它亦有机制，其一便是@propery关键字。用此关键字，其获取、设置函数，须与属性名一致。
@property可以把一个实例方法变成其同名属性，以支持.号访问，它亦可标记设置限制，加以规范，如下代码：

```python
class Animal(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._color = 'Black'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, basestring):
            self._name = value
        else:
            self._name = 'No name'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0 and value < 100:
            self._age = value
        else:
            self._age = 0
            # print 'invalid age value.'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value;
    

a = Animal('black dog', 3)
a.name = 'white dog'
a.age = 300
print 'Name:', a.name
print 'Age:', a.age
```

它以一个函数形式，定义一个属性，与@property实现原理类似，或者就是它的的变异用法。
其原型为：
```python
property(fget=None, fset=None, fdel=None, doc=None)
```

```python
class Animal(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._color = 'Black'

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, basestring):
            self._name = value
        else:
            self._name = 'No name'

    name = property(fget=get_name, fset=set_name, fdel=None, doc='name of an animal')

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value > 0 and value < 100:
            self._age = value
        else:
            self._age = 0
            # print 'invalid age value.'

    age = property(fget=get_age, fset=set_age, fdel=None, doc='name of an animal')
    

a = Animal('black dog', 3)
a.name = 'white dog'
a.age = 3
print 'Name:', a.name
print Animal.name.__doc__
print 'Age:', a.age
```