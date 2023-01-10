import sys
import heapq
from collections import deque
import copy

sys.setrecursionlimit(10**5)


def rotate(diff):

    left_up = arr[diff][diff]
    right_down = arr[n - 1 - diff][m - 1 - diff]
    for i in range(0, m - diff * 2 - 1, 1):
        # 위쪽
        up_dir = diff + i
        arr[diff][up_dir] = arr[diff][up_dir + 1]
        # 아래쪽
        down_dir = diff + i
        down_x = n - diff - 1
        down_y = m - 1
        arr[down_x][down_y - down_dir] = arr[down_x][down_y - down_dir - 1]

    for i in range(1, n - diff * 2 - 1, 1):
        # 왼쪽
        left_dir = diff + i
        arr[n - left_dir][diff] = arr[n - left_dir - 1][diff]
        # 오른쪽
        right_dir = diff + i
        right_x = m - diff - 1
        arr[right_dir - 1][right_x] = arr[right_dir][right_x]
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
    cnt = (m - (i * 2)) + (n - (i * 2)) - 4
    for k in range(r):
        rotate(i)

for o in range(n):
    print(*arr[o])