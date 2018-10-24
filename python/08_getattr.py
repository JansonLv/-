class Stu(object):
    name = ""
    age = 10

    def __getattr__(self, item):
        print(f"{item} 不存在")


s = Stu()
s.nian

