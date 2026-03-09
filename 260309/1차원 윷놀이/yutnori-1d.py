N, M, K = map(int, input().split())
nums = list(map(int, input().split()))


pos = [1] * (K)

answer = 0

def back(turn, score):
    global answer

    if turn == N:
        answer = max(answer, score)
        return 

    move = nums[turn]
    for i in range(K):
        old = pos[i]
        if old == M : 
            back(turn+1 , score)
        new = old + move
        flag = 0

        if new >= M:
            new = M
            flag = 1
        pos[i] = new
        back(turn +1, score + flag)
        pos[i] = old

back(1,0)
print(answer)