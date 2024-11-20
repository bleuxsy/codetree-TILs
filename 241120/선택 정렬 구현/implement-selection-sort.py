n = int(input())
mylist = list(map(int,input().split()))
first = max(mylist)
mylist.sort()
for i in mylist:
    print(i,end=" ")
    