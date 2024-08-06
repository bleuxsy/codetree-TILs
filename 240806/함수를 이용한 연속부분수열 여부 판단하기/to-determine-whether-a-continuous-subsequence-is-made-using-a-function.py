def yeonsok(A,B):
    for i in range(len(A) - len(B)+1):
        if A[i:i+len(B)] == B:
            return True
    return False

    
                
a , b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int,input().split()))
if yeonsok(A , B):
    print("Yes")
else:
    print("No")