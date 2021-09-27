n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i] < m:
        print(arr[i], end=' ')
