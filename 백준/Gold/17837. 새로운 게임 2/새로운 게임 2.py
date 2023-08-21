import sys

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[0 for i in range(N + 1)] for i in range(N + 1)]
horse_arr = [[[] for i in range(N + 1)] for i in range(N + 1)]
horse = [[] for i in range(K)]
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        arr[i + 1][j + 1] = a[j]
for i in range(K):
    x, y, d = map(int, input().split())
    horse[i] = [x, y, d]
    horse_arr[x][y].append(i)


# 1 빨강
# 이동한 후 이동한 말과
# 모든 말의 쌓여 있는 순서를 반대로 한다
# 2 파랑
# 이동 방향을 반대로 바꾸고
# 한 칸 이동 , 이동하려는 칸이 파란색이면 이동안함
def move():
    global res
    for i in range(K):
        x, y, d = horse[i]
        nx = x + dx[d]
        ny = y + dy[d]

        if (0 >= nx or N < nx or 0 >= ny or N < ny) or arr[nx][ny] == 2:
            d = get_dir(d)
            nx = x + dx[d]
            ny = y + dy[d]
            horse[i][2] = d
            if (0 >= nx or N < nx or 0 >= ny or N < ny) or arr[nx][ny] == 2:
                nx = x
                ny = y
        if nx == x and ny == y:
            continue

        idx = horse_arr[x][y].index(i)
        for j in range(idx, len(horse_arr[x][y])):
            horse[horse_arr[x][y][j]][0] = nx
            horse[horse_arr[x][y][j]][1] = ny
        if arr[nx][ny] == 0:
            horse_arr[nx][ny] += horse_arr[x][y][idx:]
            horse_arr[x][y] = horse_arr[x][y][:idx]

        if arr[nx][ny] == 1:
            horse_arr[nx][ny] += horse_arr[x][y][idx:][::-1]
            horse_arr[x][y] = horse_arr[x][y][:idx]

        if len(horse_arr[nx][ny]) >= 4:
            print(res + 1)
            exit()


def get_dir(dir):
    if dir == 1:
        return 2
    if dir == 2:
        return 1
    if dir == 3:
        return 4
    return 3


res = 0
# 오 왼 위 아래
for i in range(1000):
    res = i
    move()

print(-1)
