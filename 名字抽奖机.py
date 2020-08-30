import xlrd, random


class Game:
    def __init__(self, num, name_list):
        self.num = num
        self.name = name_list

    def excel(self):
        excel = xlrd.open_workbook(r'C:\Users\Administrator\Documents\Tencent Files\317742145\FileRecv\1.xls', encoding_override='utf8')
        table = excel.sheets()[1]
        col = table.col_values(0)
        new_col = filter(None, col)
        new_col2 = list(new_col)
        name_dic = {}
        for i in range(50):
            name_dic[i+1] = new_col2[i]
        return name_dic

    def name_excel(self):
        name_dic2 = self.excel().copy()
        name_num = []
        for n in self.name:
            for key, value in name_dic2.items():
                if value == n:
                    name_num.append(key)
        for i in name_num:
            name_dic2.pop(i)
        return name_dic2

    def one(self):
        number = list(self.name_excel().keys())
        list2 = random.sample(number, self.num)
        return list2

    def work(self):
        for i in self.one():
            print(i, ":", self.name_excel()[i])

    def judge_name(self):
        for name in self.name:
            if name not in self.excel().values():
                print('名字错误！！！')
                exit()
            elif name == '':
                pass
            else:
                pass

    def main(self):
        if not self.name:
            self.judge_name()
        else:
            pass
        self.excel()
        self.name_excel()
        self.one()
        self.work()


print("你需要抽取几个同学？")
num1 = int(input())
print("有哪些同学不参加这次抽奖？(有多个同学的时候中间用空格分开!!!)")
name = input()
game = Game(num1, name.split(' '))
game.main()