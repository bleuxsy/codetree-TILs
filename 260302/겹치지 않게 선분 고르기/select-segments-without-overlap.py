def back(idx, last_end, cnt):
    global max_count
    if idx == n:
        max_count = max(cnt, max_count)
        return
    back(idx+1, last_end, cnt)

    start, end = x[idx]
    if start > last_end :
        back(idx+1, end , cnt+1)




from collections import deque
n = int(input())
x1, x2 = [], []
x = []
for _ in range(n):
    x.append(list(map(int, input().split())))
  
x.sort(key = lambda i : (i[0], i[1]))
max_count = 0
# Please write your code here.

back(0, -float('inf'), 0)

print(max_count)