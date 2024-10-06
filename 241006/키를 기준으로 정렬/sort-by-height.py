class Student :
    def __init__(self,name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
N = int(input())
students =[]
for i in range(N):
    name, height, weight = input().split()
    students.append(Student(name, height,weight))
students.sort(key = lambda x: x.height)
for student in students:
    print(student.name, student.height, student.weight)