def solution(n):
    a = n//10
    b = n % 10 
    
    if b%2 == 0 and  (a+b)%5 == 0:
        com = 'Yes'
    else:
        com = 'No'
    return com


n = int(input())
print(solution(n))