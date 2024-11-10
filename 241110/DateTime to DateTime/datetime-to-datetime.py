a ,b,c = map(int,input().split())
if a < 11 : 
    print(-1)
elif a == 11 and b < 11:
    print(-1)
else:
    num =(a*24*60+b*60+c) -(11*24*60+11*60+11)
    print(num)