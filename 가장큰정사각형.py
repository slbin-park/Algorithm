import sys

input = sys.stdin.readline
answer = 0
n, m = map(int, input().split())
arr = [[0 for i in range(m)] for j in range(n)]
flag = 0
for i in range(n):
    a = input().strip()
    for j in range(m):
        arr[i][j] = int(a[j])
        if int(a[j]) == 1:
            flag = 1
            answer = 1
if n < 2 or m < 2:
    if 1 in sum(arr, []):
        print(1)
        exit(0)
    else:
        print(0)
        exit(0)
if flag == 0:
    print(0)
    exit(0)
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i][j - 1], arr[i - 1][j],
                            arr[i - 1][j - 1]) + 1
            answer = max(answer, arr[i][j])
print(answer**2)