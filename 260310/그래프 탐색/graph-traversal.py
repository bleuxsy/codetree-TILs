def dfs(cur, total ):
    best = total 
    
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            best = max(best , dfs(nxt, total+1))
            visited[nxt] = False


    return best

            

#### 1 ----> 2


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * ( n + 1)
answer = 0
# Please write your code here.
visited[1] = True
answer = dfs(1, 0)
print(answer)