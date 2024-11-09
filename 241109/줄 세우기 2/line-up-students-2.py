N = int(input())


students = []
for i in range(N):
    h, w = map(int, input().split())
    students.append((h, w, i + 1))  


students.sort(key=lambda x: (x[0], -x[1]))


for h, w, num in students:
    print(h, w, num)