def threesixnin(n):
    x = n//10
    y = n %10
    return x%3==0 or y%3==0
def threemul(n):
    return n%3==0


a,b = map(int,input().split())
cnt = 0
for num in range(a,b+1):
    if threesixnin(num) or threemul(num):
        cnt+=1
print(cnt)