class Student:
    def __init__(self):
        self.student_list = {}

    def show(self):
        print('{:16s}{:16s}{:8s}{:4s}'.format('No', 'Name', 'Gender', 'Age'))
        for key, value in self.student_list.items():
            print('{:16s}{:16s}{:8s}{:4s}'.format(str(key), str(value[0]), str(value[1]), str(value[2])))

    def insert(self, no, name, gender, age):
        if gender == '男' or gender == '女':
            self.student_list[no] = [name, gender, age]
            print("添加成功")
        else:
            print("性别输入错误")

    def update(self, no, name, gender, age):
        if gender == '男' or gender == '女':
            self.student_list[no] = [name, gender, age]
            print("修改成功")
        else:
            print("性别错误")

    def delete(self, no):
        if no in list(self.student_list.keys()):
            del self.student_list[no]
            print("删除成功")
        else:
            print("该学生不存在")

    def attempt(self):
        while True:
            a = input("> ")
            if a == 'insert':
                no = int(input('NO:'))
                if no in list(self.student_list.keys()):
                    print("这个序号已经存在")
                else:
                    name = input('Name:')
                    gender = input('Gender:')
                    age = input('Age:')
                    self.insert(no, name, gender, age)
            elif a == 'update':
                no = int(input('No:'))
                if no not in list(self.student_list.keys()):
                    print("该学生不存在")
                else:
                    name = input('Name:')
                    gender = input('Gender:')
                    age = input('Age:')
                    self.update(no, name, gender, age)
            elif a == 'delete':
                no = int(input('No:'))
                self.delete(no)
            elif a == 'show':
                self.show()
            elif a == 'exit':
                exit()
            else:
                print('show   -> 查看表数据')
                print('insert -> 插入学生信息数据')
                print('update -> 更新学生信息数据')
                print('delete -> 删除学生信息数据')


s1 = Student()
s1.attempt()