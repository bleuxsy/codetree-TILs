def onjun(N):
    if N%2 == 0:
        return False
    elif N%10 == 5:
        return False
    elif N%3 == 0 and N%9 !=0:
        return False
    return True
a, b = map(int, input().split())
count = 0
for i in range(a, b+1):
    if onjun(i):
        count += 1
print(count)