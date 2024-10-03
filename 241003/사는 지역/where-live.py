class Student:
    def __init__(self, name, phone, city):
        self.name = name
        self.phone = phone
        self.city = city

N = int(input())
students = []
for i in range(N):
    name, phone, city = input().split()
    students.append(Student(name, phone, city))

# students 리스트를 name 기준으로 정렬
students_sorted = sorted(students, key=lambda student: student.name)

# 정렬된 리스트의 마지막 학생 정보 출력
print(f'name {students_sorted[-1].name}')
print(f'addr {students_sorted[-1].phone}')
print(f'city {students_sorted[-1].city}')