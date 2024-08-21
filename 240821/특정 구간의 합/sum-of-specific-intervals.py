def solution(A, m):
    num = 0
    a, b = map(int,input().split())
    for i in range(a-1,b):
        num += A[i]
    print(num)

n, m = map(int,input().split())
A = list(map(int,input().split()))
for i in range(m):
    solution(A,m)