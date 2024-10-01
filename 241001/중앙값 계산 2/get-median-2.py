n = int(input())
mylist= list(map(int,input().split()))
i= 0 
sublist=[]
while(n>i):
    if i == 0 :
        print(mylist[0],end=' ')
        i+=1
        continue;
    elif i%2 == 0:
        sublist= sorted(mylist[:i+1])
        print(sublist[i//2],end=' ')
    i+=1