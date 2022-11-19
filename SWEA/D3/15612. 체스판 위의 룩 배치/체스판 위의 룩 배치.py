dx = [0,0,1,-1]
dy = [1,-1,0,0]
dic = {}
n = int(input())
def bfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0<= nx < 8 and 0<= ny < 8:
            if arr[nx][ny] =="O":
                return False;
            nx += dx[i]
            ny += dy[i]
    return True
index = 1
for i in range(n):
    arr = [[""for _ in range(8)]for _ in range(8)]
    visited = [[0 for _ in range(8)]for _ in range(8)]
    for j in range(8):
        a = input()
        for k in range(8):
            arr[j][k] = a[k]
    cnt = 0
    flag = 0
    for j in range(8):
        for k in range(8):
            if arr[j][k] == "O":
                cnt+=1
                if bfs(j,k):
                    continue
                flag=1
                break;
    if flag== 0 and cnt==8:
        print("#",end="")
        print(index,end="")
        print(" ",end="")
        print("yes")
    else:
        print("#",end="")
        print(index,end="")
        print(" ",end="")
        print("no")
    index+=1