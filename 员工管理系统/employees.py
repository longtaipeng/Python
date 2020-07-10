class Employees:
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return '{:8s}{:8s}{:8s}'.format(self.name, self.gender, self.tel)

