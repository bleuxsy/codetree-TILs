N = int(input())
mylist = list(map(int,input().split()))
mylist.sort()
total = 0
for i in range(N):
    total= max(total,(mylist[i]+mylist[-1-i]))
print(total)