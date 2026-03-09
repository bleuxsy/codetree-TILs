n = int(input())
visited = [False] * (n+1)
answer = []
# Please write your code here.
def back(L):
    
    if L == n+1:
        print(*answer)
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)
        back(L+1)
        visited[i] = False
        answer.pop()

    







back(1)