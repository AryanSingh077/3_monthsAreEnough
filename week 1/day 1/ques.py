class Student:
    college = "MMMUT"

    @classmethod
    def change_college(cls, name):
        cls.college = name

Student.change_college("NIT")
print(Student.college)
