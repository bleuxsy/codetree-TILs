def solution(a):
    return a*a
n = input()
total=0
for i in n:
    total += solution(int(i))
print(total)