def yesno(A):
    for i in A:
        if A[0] != i:
            return True
    return False
A = input()
if yesno(A):
    print("Yes")
else:
    print("No")