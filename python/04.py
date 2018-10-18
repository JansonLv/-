

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
