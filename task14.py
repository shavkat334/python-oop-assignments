class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_info(self) -> None:
        print(f"Student(name='{self.name}', age{self.age})")

s01 = Student('ali', 13)
s02 = Student('vali', 14)
s03 = Student('gani', 16)
s04 = Student('sami', 11)
s05 = Student('joni', 10)

students: list[Student] = [s01,s02, s03, s04, s05]

min_student = min(students, key=lambda s: s.age)
min_student.show_info()