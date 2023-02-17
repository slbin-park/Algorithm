import sys
from collections import deque
import heapq

input = sys.stdin.readline


def is_end(nx, ny):
    if 0 <= nx < n and 0 <= ny < n:
        if arr[nx][ny] == 0 or arr[nx][ny] == 5:
            return True
    return False


dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
cur_dir = 100
n = int(input())
arr = [[0 for i in range(n)] for i in range(n)]
k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    # 사과 위치 저장
    arr[a - 1][b - 1] = 5
l = int(input())
dq = deque()
for i in range(l):
    a, b = map(str, input().split())
    a = int(a)
    dq.append([a, b])
time = 0
arr[0][0] = 1
head = [0, 0]
tail = [0, 0]
# 사과는 5
while True:
    time += 1
    nx, ny = 0, 0
    if len(dq) and dq[0][0] + 1 == time:
        xd, t = dq.popleft()
        if (t == "L"):
            cur_dir += 1
        if (t == "D"):
            cur_dir -= 1
    # 진행해야하는 다음 방향
    nx = head[0] + dir[cur_dir % 4][0]
    ny = head[1] + dir[cur_dir % 4][1]
    # print("time = ", time)
    # print("head = ", head, cur_dir)
    # print("tail = ", tail)
    # print("cur_dir = ", cur_dir)
    # print(nx, ny)
    if not is_end(nx, ny):
        break
    # 저장된곳은 다음으로 이동할 방향을 저장함
    arr[head[0]][head[1]] = cur_dir % 4 + 1
    # 머리 한칸 이동
    head = [nx, ny]
    #사과가 아니라면 꼬리 0으로 변경
    if arr[nx][ny] != 5:
        get_next_dir = arr[tail[0]][tail[1]] - 1
        arr[tail[0]][tail[1]] = 0
        tail[0] += dir[get_next_dir][0]
        tail[1] += dir[get_next_dir][1]
print(time)
