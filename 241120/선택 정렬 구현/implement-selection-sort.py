n = int(input())
arr = list(map(int,input().split()))

def selection_sort():
    for i in range(n-1):
        min_index = i
        for k in range(i+1, n):
            if arr[min_index] > arr[k]:
                min_index = k

        arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort()
for i in arr:
    print(i,end=" ")