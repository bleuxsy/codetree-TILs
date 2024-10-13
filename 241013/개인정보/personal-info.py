class Student:
    def __init__(self, name, h,w):
        self.name = name
        self.h = int(h)
        self.w= float(w)
students=[]
for i in range(5):
    name , h,w = input().split()
    students.append(Student(name,h,w))
students.sort(key = lambda student : student.name)
print("name")
for i in students:
    print(f'{i.name} {i.h} {i.w}')
print()
print("height")
students.sort(key = lambda student: -student.h)
for j in students:
    print(f'{j.name} {j.h} {j.w}')