import sys
from collections import deque

input = sys.stdin.readline
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
even = [0, 2, 4, 6]
odd = [1, 3, 5, 7]


def move_fire(nx, ny, si, di):
    for i in range(si):
        nx += dir[di][0]
        ny += dir[di][1]
        if nx == n:
            nx = 0
        if nx == -1:
            nx = n - 1
        if ny == n:
            ny = 0
        if ny == -1:
            ny = n - 1
    return nx, ny


def div_fire(x, y):
    global arr, fire
    even_cnt = 0
    odd_cnt = 0
    sum_mi = 0
    sum_si = 0
    cnt = len(arr[x][y])
    for i in range(len(arr[x][y])):
        sum_mi += arr[x][y][i][0]
        sum_si += arr[x][y][i][1]
        if arr[x][y][i][2] % 2 == 1:
            even_cnt += 1
        else:
            odd_cnt += 1

    sum_mi = sum_mi // 5
    if sum_mi == 0:
        return
    # 모두 짝수
    if even_cnt == 0 or odd_cnt == 0:
        for i in range(4):
            fire.append([x, y, sum_mi, sum_si // cnt, even[i]])
    else:
        for i in range(4):
            fire.append([x, y, sum_mi, sum_si // cnt, odd[i]])


answer = 0
n, m, k = map(int, input().split())
arr = [[[] for i in range(n)] for i in range(n)]
fire = deque()
for i in range(m):
    # x,y 질량 방향 속력
    ri, ci, mi, si, di = map(int, input().split())
    ri -= 1
    ci -= 1
    fire.append([ri, ci, mi, si, di])

for i in range(k):
    while fire:
        ri, ci, mi, si, di = fire.popleft()
        nx, ny = move_fire(ri, ci, si, di)
        arr[nx][ny].append([mi, si, di])
    # for j in range(n):
    #     print(arr[j])
    for j in range(n):
        for k in range(n):
            if len(arr[j][k]) > 1:
                div_fire(j, k)
            elif len(arr[j][k]) == 1:
                fire.append(
                    [j, k, arr[j][k][0][0], arr[j][k][0][1], arr[j][k][0][2]])
            arr[j][k] = []
while fire:
    ri, ci, mi, si, di = fire.popleft()
    answer += mi
print(answer)