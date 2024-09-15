class Student:
    def __init__(self, idd="codetree", lev="10"):
        self.idd = idd
        self.lev = lev

student1 = Student()
idd,lev = input().split()
student2 = Student(idd, lev)

# Using formatted string literals (f-strings) for exact formatting
print(f"user {student1.idd} lv {student1.lev}")
print(f"user {student2.idd} lv {student2.lev}")