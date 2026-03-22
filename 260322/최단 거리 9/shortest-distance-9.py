import heapq
from collections import deque
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
a, b = map(int, input().split())
INF = 10**18
path = [0] * (n+1)
D = [INF]* (n+1)
pq = []
graph = [[] for _ in range(n+1)]

for edge in edges:
    w = edge[2]
    x = edge[0]
    y = edge[1]
    graph[x].append((y, w))

D[a] = 0
heapq.heappush(pq, (0, a))
visited = [False] *(n+1)
while pq:
    cw , cx = heapq.heappop(pq)

    if visited[cx]:
        continue
    visited[cx] = True
    for nx , nw in graph[cx]:
        if D[nx] > D[cx] + nw:
            D[nx] = D[cx] + nw
            path[nx] = cx
            heapq.heappush(pq, (D[nx], nx))


answer = []
x = b
answer.append(x)
while x != a:
    x = path[x]
    answer.append(x)

print(D[b])
for a in answer[::-1]:
    print(a , end=" ")