n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))
utemp = 0
dtemp = 0
# Please write your code here.
for _ in range(t):
    utemp = u[-1]
    dtemp= d[-1]
    
    for i in range(n-1, 0, -1):
        u[i] = u[i-1]
        d[i] = d[i-1]
    u[0] = dtemp
    d[0] = utemp

print(*u)
print(*d)