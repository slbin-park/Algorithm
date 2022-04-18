import heapq
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    heapq.heappush(arr, [start, end])
arr.sort()

res = 0
computer = [0 for i in range(n)]
cnt = [0 for i in range(n)]
for start, end in arr:
    for i in range(n):
        if computer[i] == 0:
            computer[i] = end
            cnt[i] += 1
            res += 1
            break
        elif computer[i] <= start:
            computer[i] = end
            cnt[i] += 1
            break
print(res)
for i in range(res - 1):
    print(cnt[i], end=' ')
print(cnt[res - 1])
