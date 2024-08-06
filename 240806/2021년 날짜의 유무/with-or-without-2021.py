def is_date(m,d):
    if m in [1,3,5,7,8,10,12]:
        if d <32:
            return True
    elif m in [4,6,9,11]:
        if d < 31:
            return True
    elif m == 2:
        if d<29:
            return True
    return False

M, D = map(int, input().split())
if is_date(M,D):
    print("Yes")
else:
    print("No")