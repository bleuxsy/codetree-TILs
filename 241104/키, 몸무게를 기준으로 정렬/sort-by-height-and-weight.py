class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = int(h)  # 키를 정수형으로 변환
        self.w = int(w)  # 몸무게를 정수형으로 변환

n = int(input())
persons = []
for i in range(n):
    name, h, w = input().split()
    persons.append(Person(name, h, w))

# 키는 오름차순(h), 몸무게는 내림차순(-w)으로 정렬
persons.sort(key=lambda person: (person.h, -person.w))

for person in persons:
    print(person.name, person.h, person.w)