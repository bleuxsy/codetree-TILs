N = int(input())
_list = list(map(int, input().split()))
for i in range(N):
    _list[i]= abs(_list[i])
for j in _list:
    print(j, end=" ")