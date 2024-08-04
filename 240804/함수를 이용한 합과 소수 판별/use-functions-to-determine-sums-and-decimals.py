def sosu(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def chak(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n = n // 10
    return digit_sum % 2 == 0

a, b = map(int, input().split())
result = 0
for i in range(a, b + 1):
    if sosu(i) and chak(i):
        result += 1
print(result)