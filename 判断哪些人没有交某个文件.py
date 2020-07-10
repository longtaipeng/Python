"""
这是一个用于匹配哪个人没有交文件的一个程序！！！
匹配前要求所有文件名的格式相同
输入三个参数就可以判断出来
这个程序里面的源文件是来自我电脑本身，在使用时请自行更改 excel 方法里面的源文件路径及其他内容
"""
import xlrd
import os


class Game:
    def __init__(self, dress, num1, str1):
        self.dress = dress
        self.num1 = int(num1)-1
        self.str1 = str1

    def excel(self):                       # 获取到全班同学的名字
        # 打开excel文件
        excel = xlrd.open_workbook(r'C:\Users\Administrator\Documents\Tencent Files\317742145\FileRecv\1.xls', encoding_override='utf8')
        table = excel.sheets()[1]         # 获取excel里面的表格
        col = table.col_values(0)         # 获取到table里面的第几列的数据内容
        return col

    def obtain_name(self):                 # 获取到指定文件夹下的同学的名字
        name_list = []
        new_name_list = []
        test_name = os.listdir(self.dress)
        for i in test_name:
            name_list.append(i[self.num1:])
        for i in name_list:
            new_name_list.append(i[:i.find(self.str1)])
        return new_name_list

    def judge(self):                     # 匹配没有出现在文件夹里面的名字
        missing_name = [name for name in self.excel() if name not in self.obtain_name()]  # 判断是否存在
        for i in missing_name:
            print(i)


print('请确保文件名字的格式相同！！！')
print('请确保文件名字的格式相同！！！')
print('请确保文件名字的格式相同！！！')
url = input('请输入文件夹的位置：')
num1 = input('请输入人名的开始是在第几位：')
str1 = input('请输入人名结束后的第一个字符是什么：')
g1 = Game(url, num1, str1)
print('以下同学没有提交文件：')
g1.judge()

