
class Gog(object):
    name = "mini"

    def __enter__(self):
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.name + "睡了")


with Gog() as d:
    print(d + "起床了")
