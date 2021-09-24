n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort(key=lambda a: a[0])
prev = arr[0][1]
prevcow = arr[0][0]
cnt = 0
for i in range(1, n):
    if arr[i][0] == prevcow and arr[i][1] != prev:
        cnt += 1
    prev = arr[i][1]
    prevcow = arr[i][0]
print(cnt)