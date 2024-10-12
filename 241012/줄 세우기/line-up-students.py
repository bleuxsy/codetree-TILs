class Student:
    def __init__(self,h,w, num):
        self.h=h
        self.w=w
        self.num = num
N = int(input())
students=[]
for i in range(1,N+1):
    h,w =map(int,input().split())
    students.append(Student(h,w,i))

students.sort( key = lambda student :(-student.h , -student.w,student.num))
for j in students:
    print(f'{j.h} {j.w} {j.num}')