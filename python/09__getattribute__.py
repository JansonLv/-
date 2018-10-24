
class Gog(object):
    name = ""

    def __getattribute__(self, item):
        print(f"{item} 已存在")


d = Gog()
d.name