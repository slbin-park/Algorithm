import sys
import heapq
from collections import deque
import copy

sys.setrecursionlimit(10**5)


def rotate(diff):
    # 가로축
    left_up = arr[diff][diff]
    right_down = arr[n - 1 - diff][m - 1 - diff]
    for i in range(0, m - diff * 2 - 1, 1):
        # 위쪽
        arr[diff][diff + i] = arr[diff][diff + i + 1]
        # 아래쪽
        arr[n - diff - 1][m - 1 - diff - i] = arr[n - diff - 1][m - 1 - diff -
                                                                1 - i]

    for i in range(1, n - diff * 2 - 1, 1):
        arr[n - i - diff][diff] = arr[n - i - 1 - diff][diff]
        arr[diff + i - 1][m - diff - 1] = arr[diff + i][m - diff - 1]
    arr[diff + 1][diff] = left_up
    arr[n - 1 - diff - 1][m - 1 - diff] = right_down


input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
prev = 0
answer = 0
n, m, r = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
r_arr = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

for i in range(min(n, m) // 2):
    for k in range(r):
        rotate(i)

for o in range(n):
    print(*arr[o])