n = int(input())
result = []
for i in range(n):
    result.append(input())
result.sort()
for i in result:
    print("".join(i))