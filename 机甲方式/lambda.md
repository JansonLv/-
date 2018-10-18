## lambda 匿名函数

lambda操作符（或lambda函数）通常用来创建小巧的，一次性的匿名函数对象。它的基本语法如下：

    lambda arguments : expression

lambda操作符可以有任意数量的参数，但是它只能有一个表达式，且不能包含任何语句，返回一个可以赋值给任何变量的函数对象。

下面通过一个例子来理解一下。首先看看一个Python函数：

    def add(x, y):    

    return x+y

    # call the function

    add(1, 2)  # Output: 3

    lambda x, y: x + y

在lambda x, y : x + y中，x和y是函数的参数，x+y是表达式，它被执行并返回结果。

lambda x, y : x + y返回的是一个函数对象，它可以被赋值给任何变量。在本例中函数对象被赋值给了add变量。如果我们查看add的type，可以看到它是一个Function。

    type(add)  # Output: function

绝大多数lambda函数作为一个参数传给一个需要函数对象为参数的函数，比如map，reduce，filter等函数。