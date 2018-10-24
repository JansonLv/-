class B():
    def __init__(self):
        self.a_list = 1
        self.b_list = 2

    def run(self):
        print(self.a_list)

    def __call__(self, *args, **kwargs):
        self.run()


if __name__ == '__main__':
    B()()
