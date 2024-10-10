class Student:
    def __init__(self, name, kor, eng, math):
        self.name= name
        self.kor = int(kor)
        self.eng = int(eng)
        self.math = int(math)
n = int(input())
students=[]
for i in range(n):
    name, kor, eng, math= input().split()
    students.append(Student(name,kor,eng,math))
students.sort(key=lambda x: (x.kor+x.eng+x.math))
for i in students:
    print(f'{i.name} {i.kor} {i.eng} {i.math}')