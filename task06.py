class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age  = age
        self.grade = grade

    def info(self) -> None:
        print(f'Student"(ismi {self.name}","yoshi {self.age}", "{self.grade} sinf oquvchisi")')
s01 = Student('ali', 20, 'A')

s01.info()



