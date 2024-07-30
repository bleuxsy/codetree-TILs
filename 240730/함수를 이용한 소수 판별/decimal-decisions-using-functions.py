def is_prim(n):
    for i in range(2, n):
        if n%i != 0 :
            continue
        else : 
            return 0
    return n
            

a, b = map(int, input().split())
sum = 0 
for i in range(a,b+1):
    sum += is_prim(i)
print(sum)