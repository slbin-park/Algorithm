def solution(commands):
    answer = []
    N = 51
    arr = [['' for i in range(N)] for i in range(N)]
    parent = [[[j, i] for i in range(N)] for j in range(N)]
    merge = [["UM" for i in range(N)] for j in range(N)]

    def find(x, y):
        if parent[x][y] != [x, y]:
            parent[x][y] = find(parent[x][y][0], parent[x][y][1])
            return parent[x][y]
        return parent[x][y]

    def union(x1, y1, x2, y2):
        parent[x2][y2] = parent[x1][y1]
        merge[x1][y1] = 1

    for i in range(len(commands)):
        cmd = commands[i].split(' ')
        if cmd[0] == "UPDATE" and len(cmd) == 4:
            r1, c1 = int(cmd[1]), int(cmd[2])
            r, c = find(r1, c1)
            merge[r][c] = "UP"
            arr[r][c] = cmd[3]

        # 전체 변경
        if cmd[0] == "UPDATE" and len(cmd) == 3:
            for j in range(N):
                for k in range(N):
                    if arr[j][k] == cmd[1]:
                        arr[j][k] = cmd[2]

        if cmd[0] == "MERGE":
            r1, c1, r2, c2 = map(int, cmd[1:])
            r1, c1 = find(r1, c1)
            r2, c2 = find(r2, c2)
            r, c = r1, c1
            if arr[r1][c1] == "":
                r, c = r2, c2
            for j in range(N):
                for k in range(N):
                    if find(j,k)  == [r1,c1] or find(j,k) == [r2,c2]:
                        parent[j][k] = [r,c]
            merge[r][c] = "UP"

        if cmd[0] == "UNMERGE":
            r1, c1 = map(int, cmd[1:])
            r, c = find(r1, c1)
            prev_v = arr[r][c]
            parent[r1][c1] = [r1, c1]
            for j in range(N):
                for k in range(N):
                    if find(j, k) == [r, c]:
                        merge[j][k] = "UM"
                        parent[j][k] = [j, k]
                        arr[j][k] = ""
            arr[r1][c1] = prev_v
            merge[r1][c1] = "UP"

        if cmd[0] == "PRINT":
            r1, c1 = map(int, cmd[1:])
            r, c = find(r1, c1)
            flag = 0
            # print("========arr========")
            # for i in range(len(arr)):
            #     print(arr[i])
            # print("========parent========")
            # for i in range(len(parent)):
            #     print(parent[i])
            # print("========merge========")
            # for i in range(len(merge)):
            #     print(merge[i])
            # print(r, c)
            if arr[r][c] == "":
                answer.append("EMPTY")
            else:
                if merge[r][c] == "UM":
                    answer.append("EMPTY")
                else:
                    answer.append(arr[r][c])
    return answer