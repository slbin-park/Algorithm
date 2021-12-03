import sys

input = sys.stdin.readline

n = int(input())
dx = [-1, 0]
dy = [0, -1]

arr = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))
cnt = [[[0, 3] for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            cnt[i][j] = [1, 0]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if cnt[nx][ny][1] == 2 and cnt[nx][ny][1] != 3:
                        if cnt[i][j][0] < cnt[nx][ny][0] + 1:
                            cnt[i][j] = [cnt[nx][ny][0] + 1, arr[i][j]]
                    elif cnt[i][j][0] < cnt[nx][ny][0]:
                        cnt[i][j] = cnt[nx][ny]
        if arr[i][j] == 1:
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if cnt[nx][ny][1] == 0 and cnt[nx][ny][1] != 3:
                        if cnt[i][j][0] < cnt[nx][ny][0] + 1:
                            cnt[i][j] = [cnt[nx][ny][0] + 1, arr[i][j]]
                    elif cnt[i][j][0] < cnt[nx][ny][0]:
                        cnt[i][j] = cnt[nx][ny]
        if arr[i][j] == 2:
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if cnt[nx][ny][1] == 1 and cnt[nx][ny][1] != 3:
                        if cnt[i][j][0] < cnt[nx][ny][0] + 1:
                            cnt[i][j] = [cnt[nx][ny][0] + 1, arr[i][j]]
                    elif cnt[i][j][0] < cnt[nx][ny][0]:
                        cnt[i][j] = cnt[nx][ny]
print(cnt[n - 1][n - 1][0])
