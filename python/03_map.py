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


a = [1, 2, 3, 4, 5, 6]

x = filter(lambda x : x % 2 == 0, a)
print(list(x))
# Output: [2, 4, 6]