import random


class Game:
    def __init__(self, num):
        self.num = num

    def one(self):
        list1 = []
        for i in range(self.num):
            list1.append(random.randint(1, 50))
        return list(set(list1))

    def two(self):
        list2 = self.one()
        if len(list2) == self.num:
            print(list2)
        else:
            self.one()
            self.two()


print("你需要抽取几个同学？")
num1 = int(input())
game = Game(num1)
game.one()
game.two()