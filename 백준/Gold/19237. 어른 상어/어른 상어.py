import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

TIME = 0
N, M, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]
smell = [[deque() for _ in range(N)] for _ in range(N)]
shark = [[[]] for i in range(M + 1)]  # 상어 방향 우선 순위
shark_dir = [0] * (M + 1)  # 현재 상어 방향
shark_location = [[0, 0]] * (M + 1)  # 상어 위치
alive_shark = [M - i for i in range(M)]
prev_shark_location = [[]] * (M + 1)
tmp_smell = []
die_shark = []

for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        arr[i][j] = a[j]
        if a[j] != 0:
            shark_location[a[j]] = [i, j]
tmp = list(map(int, input().split()))

for i in range(1, M + 1):
    shark_dir[i] = tmp[i - 1]

for i in range(M):
    for j in range(4):
        shark[i + 1].append(list(map(int, input().split())))


# smell = [시간,상어 번호]
def print_dir(dir):
    if dir == 1:
        print("보는 방향 = 위")
    if dir == 2:
        print("보는 방향 = 아래")
    if dir == 3:
        print("보는 방향 = 왼쪾")
    if dir == 4:
        print("보는 방향 = 오른쪽")


def find_next_location(shark_index):
    d = shark_dir[shark_index]  # 현재 방향 구함
    x, y = shark_location[shark_index]  # 현재 상어의 위치 구함
    for next_d in shark[shark_index][d]:
        # 우선 순위에 따른 다음 위치 구함
        nx = x + dx[next_d]
        ny = y + dy[next_d]

        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        dq = smell[nx][ny]
        while dq:
            k, next_shark_idx = dq[0]
            if k <= TIME:
                dq.popleft()
            else:
                break

        if len(dq) == 0:
            shark_dir[shark_index] = next_d  # 이동한 방향
            tmp_smell.append([TIME + K, shark_index, x, y])  # 냄새 남기기
            shark_location[shark_index] = [nx, ny]  # 현재 상어 위치 변경
            if arr[x][y] == shark_index:
                arr[x][y] = 0
            if arr[nx][ny] > shark_index:  # 역순으로 진행하기 때문에 나보다 번호가 큰 상어가 존재하면 잡아먹음
                die_shark.append(arr[nx][ny])
            arr[nx][ny] = shark_index  # 위치 이동
            return

    # 이동하지 못함 그럼 원래 위치로 감
    for next_d in shark[shark_index][d]:
        # 우선 순위에 따른 다음 위치 구함
        nx = x + dx[next_d]
        ny = y + dy[next_d]

        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        dq = smell[nx][ny]
        for j in range(len(dq)):
            k, idx = dq[j]
            if idx == shark_index:
                shark_dir[shark_index] = next_d  # 이동한 방향
                tmp_smell.append([TIME + K, shark_index, x, y])  # 냄새 남기기
                shark_location[shark_index] = [nx, ny]  # 현재 상어 위치 변경
                if arr[x][y] == shark_index:
                    arr[x][y] = 0
                if arr[nx][ny] > shark_index:  # 역순으로 진행하기 때문에 나보다 번호가 큰 상어가 존재하면 잡아먹음
                    die_shark.append(arr[nx][ny])
                arr[nx][ny] = shark_index  # 위치 이동
                return


while TIME < 1001:
    TIME += 1
    die_shark = []
    tmp_smell = []
    for idx in alive_shark:
        find_next_location(idx)

    for idx in die_shark:
        x, y = shark_location[idx]
        alive_shark.remove(idx)
    for time, idx, x, y in tmp_smell:
        smell[x][y].append([time, idx])
    # print("alive = ", alive_shark)
    if len(alive_shark) == 1:
        break

    # for i in range(N):
    #     print(arr[i])

print(TIME if TIME < 1001 else -1)
