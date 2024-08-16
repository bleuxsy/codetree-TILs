def two(mylist, N):
    for i in range(N):
        if mylist[i] % 2== 0:
            mylist[i] = mylist[i]//2
        else:
            continue

N = int(input())
_list = list(map(int,input().split()))
two(_list, N)
for i in _list:
    print(i, end=" ")