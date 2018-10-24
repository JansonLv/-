class test():
    def __init__(self,data=1):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data

    def __await__(self):
        pass

    def test1(self):
        print("test")

    def test2(self):
        print("test")

print(dir(test))

for item in test(3):
    print(item)
