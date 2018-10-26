__metaclass__ = type


class Recantagle(list):
    def __init__(self):
        self.height = 0
        self.width = 0

    def getSize(self):
        return self.width, self.height

    def setSize(self, size):
        self.width, self.height = size

    size = property(getSize, setSize)


r = Recantagle()
r.setSize((10, 20))
r.getSize()


class Recantagle2(list):
    def __init__(self):
        self.height = 0
        self.width = 0
        self._name = ""

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self.width, self.height

    @name.setter
    def name(self, size):
        self.width, self.height = size




