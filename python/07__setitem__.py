class B():
    def __init__(self):
        self.a_list = 1
        self.b_list = 2

    # def __delitem__(self, key):
    #     del self.__dict__[key]
        # self.__dict__[key] = None


def cfun(a, b, c):
    a.__dict__[b] = c
    print(f"新增key:{b}, value:{c}")


if __name__ == '__main__':
    b = B()
    print(b.a_list)
    del b.a_list
    print(b.a_list)
