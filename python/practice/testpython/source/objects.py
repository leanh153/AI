
class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def change_id(self, id):
        self.id = id

    def __getattribute__(self, item):
        return self.name

    def print(self):
        print("{} - {}".format(self.name, self.id))


s = Student("le van anh", 1)
s1 = Student("le van em", 2)
s2 = Student("le van be", 3)

s1.print()
s2.print()
s.print()
