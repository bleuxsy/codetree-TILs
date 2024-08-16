def swap(a,b):
    a,b = b, a
    return a , b
a, b = map(int, input().split())
a, b = swap(a,b)
print(a, b)