def modify_numbers(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        b += 25
        a *= 2
    return a, b

# 함수 호출 및 결과 출력
a, b = map(int,input().split())
a, b = modify_numbers(a, b)
print(a, b)