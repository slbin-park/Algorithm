import sys
from collections import deque

input = sys.stdin.readline

d_left = [[-1, 0], [1, 0], [-1, -1], [1, -1], [-2, -1], [2, -1], [-1, -2],
          [1, -2], [0, -3]]
d_per = [0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05]
d_L = [0, -2]

d_down = [[0, 1], [0, -1], [1, -1], [1, 1], [1, -2], [1, 2], [2, 1], [2, -1],
          [3, 0]]
d_A = [2, 0]

d_right = [[1, 0], [-1, 0], [1, 1], [-1, 1], [-2, 1], [2, 1], [-1, 2], [1, 2],
           [0, 3]]
d_R = [0, 2]

d_up = [[0, 1], [0, -1], [-1, -1], [-1, 1], [-1, 2], [-1, -2], [-2, -1],
        [-2, 1], [-3, 0]]
d_U = [-2, 0]
answer = 0


def get_cnt(r, c):
    global answer
    # 왼쪽
    if dir == 0:
        cur_sum = 0
        if not 0 <= r < n or not 0 <= c - 1 < n:
            return
        cur_v = arr[r][c - 1]
        for i in range(9):
            nx = r + d_left[i][0]
            ny = c + d_left[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] += int(cur_v * d_per[i])
                cur_sum += int(cur_v * d_per[i])
            # 밖으로 나갔을때
            else:
                answer += int(cur_v * d_per[i])
                cur_sum += int(cur_v * d_per[i])
        rn = r + d_L[0]
        rc = c + d_L[1]
        if 0 <= rn < n and 0 <= rc < n:
            change_arr(rn, rc, cur_v, cur_sum)
        else:
            answer += cur_v - cur_sum
    if dir == 1:
        cur_sum = 0
        if not 0 <= r + 1 < n or not 0 <= c + 1 < n:
            return
        cur_v = arr[r + 1][c]
        for i in range(9):
            nx = r + d_down[i][0]
            ny = c + d_down[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] += int(cur_v * d_per[i])
                cur_sum += int(cur_v * d_per[i])
            else:
                answer += int(cur_v * d_per[i])
                cur_sum += int(cur_v * d_per[i])
        rn = r + d_A[0]
        rc = c + d_A[1]
        if 0 <= rn < n and 0 <= rc < n:
            change_arr(rn, rc, cur_v, cur_sum)
        else:
            answer += cur_v - cur_sum

    if dir == 2:
        cur_sum = 0
        if not 0 <= r < n or not 0 <= c + 1 < n:
            return
        cur_v = arr[r][c + 1]
        for i in range(9):
            nx = r + d_right[i][0]
            ny = c + d_right[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] += int(cur_v * d_per[i])
                cur_sum += int(cur_v * d_per[i])
            else:
                answer += int(cur_v * d_per[i])
                cur_sum += int(cur_v * d_per[i])
        rn = r + d_R[0]
        rc = c + d_R[1]
        if 0 <= rn < n and 0 <= rc < n:
            change_arr(rn, rc, cur_v, cur_sum)
        else:
            answer += cur_v - cur_sum

    if dir == 3:
        cur_sum = 0
        if not 0 <= r - 1 < n or not 0 <= c < n:
            return
        cur_v = arr[r - 1][c]
        for i in range(9):
            nx = r + d_up[i][0]
            ny = c + d_up[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] += int(cur_v * d_per[i])
                cur_sum += int(cur_v * d_per[i])
            else:
                answer += int(cur_v * d_per[i])
                cur_sum += int(cur_v * d_per[i])
        rn = r + d_U[0]
        rc = c + d_U[1]
        if 0 <= rn < n and 0 <= rc < n:
            change_arr(rn, rc, cur_v, cur_sum)
        else:
            answer += cur_v - cur_sum


def change_arr(rn, rc, cur_v, cur_sum):
    arr[rn][rc] += cur_v - cur_sum


# 왼쪽 , 밑 , 오른쪽 , 위쪽
move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
dir = 0
cnt = 0
move_cnt = 1
move_dir = 0
n = int(input())
arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))
r = n // 2
c = n // 2

while r != 0 or c != 0:
    # print(r, c)
    # print(answer)
    if cnt == move_cnt:
        dir += 1
        dir = dir % 4
        move_dir += 1
        cnt = 0
        if move_dir == 2:
            move_cnt += 1
            move_dir = 0
    get_cnt(r, c)
    r += move[dir][0]
    c += move[dir][1]
    arr[r][c] = 0
    cnt += 1
    # for i in range(n):
    #     print(arr[i])
print(answer)