from employees import *
import os


class EmployeesManager:
    def __init__(self):
        self.employees_list = []

    def run(self):
        self.load_employees()  # 1������Ա����Ϣ
        while True:
            # 2����ʾ���ܲ˵�
            self.show_menu()
            # 3���û����빦�����
            try:
                menu_num = int(input('����������Ҫ�Ĺ�����ţ�'))
            except:
                print('�������������1-7����ţ�')
                continue
            # 4�������û�����Ĺ������ִ�в�ͬ�Ĺ���
            if menu_num == 1:
                self.add_employees()  # �û�����1�����Ա��
            elif menu_num == 2:
                self.del_employees()  # �û�����2��ɾ��Ա��
            elif menu_num == 3:
                self.modify_employees()  # �û�����3���޸�Ա��
            elif menu_num == 4:
                self.search_employees()  # �û�����4����ѯԱ��
            elif menu_num == 5:
                self.show_employees()  # �û�����5����ʾ����Ա����Ϣ
            elif menu_num == 6:
                self.save_employees()  # �û�����6������Ա����Ϣ��ע��ǰ�����ɾ�Ĳ���������������ǲ������л����ļ���
            elif menu_num == 7:
                break  # �û�����7�����˳�����
            else:
                print('�������������1-7����ţ�')

    @staticmethod
    def show_menu():
        print('��ѡ�����¹��ܶ�Ӧ�����-------------')
        print('1:���Ա��')
        print('2:ɾ��Ա��')
        print('3:�޸�Ա����Ϣ')
        print('4:��ѯԱ����Ϣ')
        print('5:��ʾ����Ա����Ϣ')
        print('6:����Ա����Ϣ')
        print('7:�˳�ϵͳ')

    def add_employees(self):
        name = input('Name:��')
        gender = input('Gender: ')
        tel = input('Tel: ')
        self.employees_list.append(Employees(name, gender, tel))
        print(Employees(name, gender, tel))

    def del_employees(self):
        flag = False
        del_name = input('Name:��')
        for i in range(len(self.employees_list)):
            if self.employees_list[i].name == del_name:
                del self.employees_list[i]
                print("ɾ���ɹ�")
                flag = True
                break
        if not flag:
            print("���޴���")

    def modify_employees(self):
        flag = False
        modify_name = input('Name: ')
        for i in range(len(self.employees_list)):
            if self.employees_list[i].name == modify_name:
                new_gender = input('Gender: ')
                new_tel = input('Tel: ')
                del self.employees_list[i]
                self.employees_list.append(Employees(modify_name, new_gender, new_tel))
                print("������{}���Ա���{}���绰��{}".format(modify_name, new_gender, new_tel))
                flag = True
        if not flag:
            print("���޴���")

    def search_employees(self):
        flag = False
        search_name = input('Name: ')
        for i in range(len(self.employees_list)):
            if self.employees_list[i].name == search_name:
                print(self.employees_list[i])
                flag = True
        if not flag:
            print("���޴���")

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
            print('����ɹ�')

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
