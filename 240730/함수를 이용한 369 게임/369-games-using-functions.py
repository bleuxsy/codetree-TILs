def threesixnin(n):
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) % 3 ==0:
            return True
def threemul(n):
    return n%3==0


a,b = map(int,input().split())
cnt = 0
for num in range(a,b+1):
    if threesixnin(num) or threemul(num):
        cnt+=1
print(cnt)