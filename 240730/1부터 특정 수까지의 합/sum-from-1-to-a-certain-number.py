def solution(n):
    sum = 0
    for i in range(1,n+1):
        sum+= i 
        
    return (sum // 10)
N = int(input())
solution(N)