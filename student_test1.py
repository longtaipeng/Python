class Student:
    def __init__(self, no, name, gender, age):
        self.no = no
        self.name = name
        self.gender = gender
        self.age = age

    def show(self):
        print("%-16s %-16s %-8s %-4d" % (self.no, self.name, self.gender, self.age))

class StudentList:
    def __init__(self):
        self.students = []

    def show(self):
        print('%-16s %-16s %-8s %-4s' % ('no', 'name', 'gender', 'age'))
        for s in self.students:
            s.show()

    def __insert(self, s):
        i = 0
        while(i<len(self.students) and s.no>self.students[i].no):
            i = i+1
        if (i<len(self.students) and s.no==self.students[i].no):
            print(s.no+"已经存在")
            return False
        self.students.insert(i,s)
        print("增加成功")
        return True

    def __update(self, s):
        flag = False
        for i in range(len(self.students)):
            if (s.no==self.students[i].no):
                self.students[i].name = s.name
                self.students[i].gender = s.gender
                self.students[i].age = s.age
                print("修改成功")
                flag = True
                break
        if (not flag):
            print("没有这个学生")
        return flag

    def __delete(self, no):
        flag = False
        for i in range(len(self.students)):
            if (self.students[i].no == no):
                del self.students[i]
                print("删除成功")
                flag = True
                break
        if (not flag):
            print("没有这个学生")
        return flag

    def delete(self):
        no = input("no=")
        if(no!=""):
            self.__delete(no)

    def insert(self):
        no=input("no=")
        name = input("name=")
        while True:
            gender = input("gender=")
            if(gender=="男" or gender=="女"):
                break
            else:
                print("gender is not valid")
        age = input("age=")
        if(age==""):
            age = 0
        else:
            age = int(age)
        if no != "" and name != "":
            self.__insert(Student(no, name, gender, age))
        else:
            print("学号,姓名不能为空")

    def update(self):
        no=input("no=")
        name = input("name=")
        while True:
            gender = input("gender=")
            if(gender=="男" or gender=="女"):
                break
            else:
                print("gender is not valid")
        age = input("age=")
        if(age==""):
            age = 0
        else:
            age = int(age)
        if no != "" and name != "":
            self.__update(Student(no, name, gender, age))
        else:
            print("学号,姓名不能为空")

    def process(self):
        while True:
            s = input(">")
            if (s == "show"):
                self.show()
            elif (s == "insert"):
                self.insert()
            elif (s == "update"):
                self.update()
            elif (s == "delete"):
                self.delete()
            elif (s == "exit"):
                break
            else:
                print("show: show students")
                print("insert: insert a new student")
                print("update: insert a new student")
                print("delete: delete a student")
                print("exit:  exit")

st = StudentList()
st.process()
