import sys
from collections import deque
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]


# 공기랑 닿는 치즈를 dq에 넣는 bfs
def zero_bfs():
    global prev,cnt
    while z_dq:
        x,y = z_dq.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 치즈가 있을경우 dq에 넣어줌
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    dq.append([nx,ny])
                    visited[nx][ny] = 1
                    arr[nx][ny] = 0
                # 공기가 있을경우 z_dq에 넣어줌
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    z_dq.append([nx,ny])
                    visited[nx][ny] = 1
                    
    # for i in range(n):
    #     print(arr[i])
        
    if len(dq) !=0:
        prev =len(dq)
        cnt+=1 
        
        # print()
        # print(dq)
        # print(len(dq))
        # print()
        
        bfs()

def bfs():
    global prev
    cnt = 0
    while dq:
        x,y = dq.popleft()
        z_dq.append([x,y])
        visited[x][y] = 1
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0<=nx<n and 0<=ny<m:
                # 치즈가 공기에 닿일경우 
                # 1일경우는 zero_bfs 에서 다 처리함
                # 여기서는 근처에 0 있는것만 처리하면 됨
                if arr[nx][ny] == 0 and visited[nx][ny] == 0 :
                    z_dq.append([nx,ny])
                    visited[nx][ny] = 1
    zero_bfs()
                        
            
prev = 0
cnt = 0
                
n , m = map(int,input().split())
arr = [[0 for i in range(m)]for i in range(n)]
visited = [[0 for i in range(m)]for i in range(n)]
visited[0][0] = 1

for i in range(n):
    arr[i] = list(map(int,input().split()))
    
dq = deque()
z_dq =deque()
z_dq.append([0,0])


zero_bfs()
print(cnt)
print(prev)
# print('prev = ', prev)
# print('cnt = ', cnt)