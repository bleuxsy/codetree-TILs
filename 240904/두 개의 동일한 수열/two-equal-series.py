n = int(input())
alist = list(map(int,input().split()))
blist = list(map(int, input().split()))
alist.sort()
blist.sort()
if alist == blist:
    print("Yes")
else:
    print("No")