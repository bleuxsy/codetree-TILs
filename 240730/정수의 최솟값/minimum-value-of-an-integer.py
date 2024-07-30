def solution(a,b,c):
    mim=0
    mim =min(a,b,c)
    return mim
a,b,c = map(int, input().split())
print(solution(a,b,c))