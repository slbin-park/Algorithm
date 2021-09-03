import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [0 for i in range(n)]
res[0] = 1
if n == 1:
    print(0)
else:
    for i in range(n):
        for j in range(arr[i] + 1):
            if i + j < n and i + j != i and res[i] != 0:
                if res[i + j] == 0:
                    res[i + j] = res[i] + 1
                else:
                    res[i + j] = min(res[i] + 1, res[i + j])
    if res[n - 1] == 0:
        print(-1)
    else:
        print(res[n - 1] - 1)
