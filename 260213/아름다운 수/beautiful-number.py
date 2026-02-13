def num(L):
    global res
    if L == n:
        res += 1
        return
    if L > n:
        return
    for i in range(1, 5):
        num(L + i)
       
n = int(input())
res = 0
num(0)
print(res)