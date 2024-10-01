n = int(input())
mylist= list(map(int,input().split()))
mylist.sort()
i= 0 
while(n>i):
    if i == 0 :
        print(mylist[0],end=' ')
        i+=1
        continue;
    elif i%2 == 0:
        print(mylist[i//2],end=' ')
    i+=1