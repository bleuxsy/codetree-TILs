def  solution(A,m) :
    result = A[m-1]
    while m >1 :
        if m % 2 == 1:
            m-=1
            
        else:
            m//=2
        result += A[m-1]
    return result
n, m = map(int, input().split())
A = list(map(int, input().split()))
print(solution(A,m))