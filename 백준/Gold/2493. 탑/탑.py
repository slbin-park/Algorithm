import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
top = list(map(int, input().split()))
arr = [0 for i in range(n)]
res = n
n = n - 1
stack = []
while n != -1:
    if len(stack) == 0:
        stack.append([top.pop(), n])
        n -= 1
    else:
        cur = top.pop()
        while stack:
            if stack[-1][0] < cur:
                a, b = stack.pop()
                arr[b] = n + 1
            else:
                break
        stack.append([cur, n])
        n -= 1
for i in range(res - 1):
    print(arr[i], end=' ')
print(arr[-1])