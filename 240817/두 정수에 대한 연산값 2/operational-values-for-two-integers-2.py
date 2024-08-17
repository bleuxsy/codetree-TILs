def ab(A, B):
    if A>B : 
        A = A*2
        B += 10
        print( A , B)
        return 0
    else :
        A+= 10
        B*= 2
        print( A, B)
        return 0

a, b = map(int, input().split())
ab(a, b)