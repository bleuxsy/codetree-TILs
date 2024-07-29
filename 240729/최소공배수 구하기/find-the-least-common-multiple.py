n, m= map(int,input().split())
maxnum = max(n,m)
result =0
num = 1
for i in range(1,maxnum+1):
    if n%i == 0 and m%i == 0 :
        if num < i :
            num = i
result = (n//num) * (m//num) * num
print(result)