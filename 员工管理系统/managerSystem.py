from employees import *
import os


class EmployeesManager:
    def __init__(self):
        self.employees_list = []

    def run(self):
        self.load_employees()  # 1、加载员工信息
        while True:
            # 2、显示功能菜单
            self.show_menu()
            # 3、用户输入功能序号
            try:
                menu_num = int(input('请输入您需要的功能序号：'))
            except:
                print('输入错误，请输入1-7的序号：')
                continue
            # 4、根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                self.add_employees()  # 用户输入1，添加员工
            elif menu_num == 2:
                self.del_employees()  # 用户输入2，删除员工
            elif menu_num == 3:
                self.modify_employees()  # 用户输入3，修改员工
            elif menu_num == 4:
                self.search_employees()  # 用户输入4，查询员工
            elif menu_num == 5:
                self.show_employees()  # 用户输入5，显示所有员工信息
            elif menu_num == 6:
                self.save_employees()  # 用户输入6，保存员工信息，注意前面的增删改操作后如果不保存是不会序列化到文件中
            elif menu_num == 7:
                break  # 用户输入7，则退出程序
            else:
                print('输入错误，请输入1-7的序号：')

    @staticmethod
    def show_menu():
        print('请选择如下功能对应的序号-------------')
        print('1:添加员工')
        print('2:删除员工')
        print('3:修改员工信息')
        print('4:查询员工信息')
        print('5:显示所有员工信息')
        print('6:保存员工信息')
        print('7:退出系统')

    def add_employees(self):
        name = input('Name:　')
        gender = input('Gender: ')
        tel = input('Tel: ')
        self.employees_list.append(Employees(name, gender, tel))
        print(Employees(name, gender, tel))

    def del_employees(self):
        flag = False
        del_name = input('Name:　')
        for i in range(len(self.employees_list)):
            if self.employees_list[i].name == del_name:
                del self.employees_list[i]
                print("删除成功")
                flag = True
                break
        if not flag:
            print("查无此人")

    def modify_employees(self):
        flag = False
        modify_name = input('Name: ')
        for i in range(len(self.employees_list)):
            if self.employees_list[i].name == modify_name:
                new_gender = input('Gender: ')
                new_tel = input('Tel: ')
                del self.employees_list[i]
                self.employees_list.append(Employees(modify_name, new_gender, new_tel))
                print("姓名是{}，性别是{}，电话是{}".format(modify_name, new_gender, new_tel))
                flag = True
        if not flag:
            print("查无此人")

    def search_employees(self):
        flag = False
        search_name = input('Name: ')
        for i in range(len(self.employees_list)):
            if self.employees_list[i].name == search_name:
                print(self.employees_list[i])
                flag = True
        if not flag:
            print("查无此人")

    def show_employees(self):
        for i in range(len(self.employees_list)):
            print(self.employees_list[i])

    def save_employees(self):
        new_list = []
        for i in range(len(self.employees_list)):
            new_list.append(self.employees_list[i].name)
            new_list.append(self.employees_list[i].gender)
            new_list.append(self.employees_list[i].tel)
        with open(r'employees.data', 'w', encoding='utf8') as write:
            write.write('{}'.format(','.join(new_list)))
            print('保存成功')

    def load_employees(self):
        new_list = []
        if os.path.exists('employees.data'):
            with open(r'employees.data', 'r+', encoding='utf8') as read:
                data = read.read()
                for i in data.split(','):
                    new_list.append(i)
                if len(new_list) > 1:
                    for i in range(len(new_list)):
                        if i % 3 == 0:
                            self.employees_list.append(Employees(new_list[i], new_list[i + 1], new_list[i + 2]))
        else:
            with open(r'employees.data', 'w', encoding='utf8') as W:
                pass
