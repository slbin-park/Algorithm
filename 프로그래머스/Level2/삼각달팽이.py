def solution(n):
    a = 0
    for i in range(n + 1):
        a += i
    answer = [[0 for i in range(j)] for j in range(1, n + 1)]
    arr = []
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    nxt = 0  # 다음 진행방향
    cnt = 1  # 다음 숫자
    x = 0  # x 좌표
    y = 0  # y 좌표
    while 1:
        print(x, y)
        if cnt > a:
            break
        if x >= n or y > x:
            x -= dx[nxt]
            y -= dy[nxt]
            if nxt == 2:
                nxt = 0
                x += dx[nxt]
                y += dy[nxt]
            else:
                nxt += 1
                x += dx[nxt]
                y += dy[nxt]
            continue
        if answer[x][y] != 0:
            x -= dx[nxt]
            y -= dy[nxt]
            if nxt == 2:
                nxt = 0
                x += dx[nxt]
                y += dy[nxt]
            else:
                nxt += 1
                x += dx[nxt]
                y += dy[nxt]
            continue
        answer[x][y] = cnt
        x += dx[nxt]
        y += dy[nxt]
        cnt += 1
    print(answer)
    for i in range(n):
        for j in range(len(answer[i])):
            arr.append(answer[i][j])
    print(arr)

    return answer


solution(4)