import sys

input = sys.stdin.readline
n = int(input())
res = [-1 for i in range(n)]
arr = list(map(int, input().split()))
stk = []
stk.append((arr[0], 0))
for i in range(1, n):
    while stk and stk[-1][0] < arr[i]:
        num, idx = stk.pop()
        res[idx] = arr[i]
    stk.append((arr[i], i))
print(*res)