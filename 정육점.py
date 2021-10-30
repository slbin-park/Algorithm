import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0, 0] for _ in range(n)]
sum = 0  # 무게합
sum2 = 0  # 가격합
res = 1e9
for i in range(n):
    arr[i] = list(map(int, input().split()))
    sum += arr[i][0]
arr.sort(key=lambda x: (x[1], -x[0]))
# arr.sort(reverse=True, key=lambda x: x[1])
# print(arr)
if sum < m:
    print(-1)
else:
    res = sys.maxsize
    same = 0
    w = 0
    for i in range(n):
        w += arr[i][0]
        if i >= 1 and arr[i - 1][1] == arr[i][1]:
            same += arr[i][1]
        else:
            same = 0
        if w >= m:
            res = min(res, arr[i][1] + same)
    print(res)