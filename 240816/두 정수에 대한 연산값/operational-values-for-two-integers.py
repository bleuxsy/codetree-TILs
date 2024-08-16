def maxx(a,b):
    if a> b:
        a+=25
        b*=2
    else:
        b+= 25
        a*=2
    return print(a,b)
a, b = map(int, input().split())
maxx(a,b)