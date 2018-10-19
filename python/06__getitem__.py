import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

# 具名元组动态创建一个类Card，并含有两个属性rank和suit
# 用以构建只有少数属性但是没有方法的对象

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 扑克牌2到A组成的列表
    suits = 'spades diamonds clubs hearts'.split()  # 四种花色

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]  # 笛卡尔积，13*4=52(除去两个王)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # 调用f[0]时会进入
        return self._cards[position]


if __name__ == '__main__':
    f = FrenchDeck()

    print(f[0])
    # 在这里f[0]实际是f.__getitem__(0)