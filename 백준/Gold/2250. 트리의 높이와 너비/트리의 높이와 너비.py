import sys
sys.setrecursionlimit(10**5)


def dfs(child,depth):
    # 둘 다 0일 경우에 마지막 노드임
    if arr[child][0] == -1 and arr[child][1] == -1:
        change(depth)
    # 왼쪽 노드만 없을경우
    # 값을 변경해주고 dfs 돌림
    elif arr[child][0] == -1:
        change(depth)
        dfs(arr[child][1],depth+1)
    # 오른쪽 노드만 없을경우
    # 왼쪽으로 끝까지 내려 간 뒤 값을 변경
    elif arr[child][1] == -1:
        dfs(arr[child][0],depth+1)
        change(depth)
    # dfs를 왼쪽 먼저 돌리고
    # 자신의 값으로 depth랑 위치를 지정함
    # 그 후에 오른쪽을 돔
    else:
        dfs(arr[child][0],depth+1)
        change(depth)
        dfs(arr[child][1],depth+1)

def change(depth):
    global cnt
    l_r[depth][0] = min(l_r[depth][0],cnt)
    l_r[depth][1] = max(l_r[depth][1],cnt)
    cnt+=1
    
    
cnt = 0
input = sys.stdin.readline
n = int(input())
arr = [[]for i in range(n+1)]
l_r = [[1e9,0]for i in range(n+1)]
parent = [0 for i in range(n+1)]
for i in range(n):
    inp = list(map(int,input().split()))
    if inp[1] != -1:
        parent[inp[1]] = inp[0]
    if inp[2] != -1:
        parent[inp[2]] = inp[0]
    
    arr[inp[0]] = [inp[1],inp[2]]
r_node = 0
for i in range(1,n+1):
    if parent[i] == 0:
        r_node = i
dfs(r_node,0)
index = -1
max_l = -1
for i in range(n):
    if max_l < l_r[i][1]-l_r[i][0]+1:
        index = i+1
        max_l = l_r[i][1]-l_r[i][0]+1
print(index,max_l)
