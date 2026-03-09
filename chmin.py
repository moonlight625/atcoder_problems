n, x = map(int, input().split())
arr = list(map(int, input().split()))
i = 0

for i in range(n):
    if arr[i] < x :
        print(1)
        x = arr[i]
    else:
        print(0)
    i += 1
