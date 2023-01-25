import sys
import heapq
import math
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
INF = 1e9


def mip():
    return map(int, input().split())


def lip():
    return list(map(int, input().split()))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [0] * 4000001
arr = []
n = int(input())
if n == 1:
    print(0)
    exit()
for i in range(2, n + 1):
    if visited[i] == 1:
        continue
    arr.append(i)
    for j in range(i, n + 1, i):
        visited[j] = 1
left = 0
right = 0
cur_sum = arr[0]
answer = 0
while right < len(arr):
    if cur_sum == n:
        answer += 1
        right += 1
        if right == len(arr):
            break
        cur_sum += arr[right]
    elif cur_sum > n:
        cur_sum -= arr[left]
        left += 1
    else:
        right += 1
        if right == len(arr):
            break
        cur_sum += arr[right]
print(answer)