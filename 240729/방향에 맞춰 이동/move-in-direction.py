N = int(input())
x=0
y=0
for i in range(N):
    direction, num =input().split()
    num = int(num)
    if direction == 'W':
        x-=num
    elif direction == 'S':
        y-=num
    elif direction == 'N':
        y+=num
    else:
        x+=num
print(x, y)