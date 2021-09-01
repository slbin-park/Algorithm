import sys
from collections import deque
input = sys.stdin.readline

def dfs(x):#너비우선 탐색
    visited = [0] *n #방문 노드 표시
    visited[x] = 1 #x방문 표시
    dq.append(x) #큐에 x넣기
    while dq:
        x = dq.popleft()
        for i in friends[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                dq.append(i)
    return visited


n = int(input())
m = int(input())
friends = [[]for i in range(n)]
dq = deque()
cnt = 0 #친구를 count 하기위해서
for i in range(m):
    a , b = map(int,(input().split()))
    #양방향으로 이어져있다는거하기 위해서
    friends[a-1].append(b-1)# a-1이 b-1이랑 이어져있다
    friends[b-1].append(a-1)# b-1이 a-1이랑 이어져있다

result = dfs(0)
for i in result:
    if 1 < i <=3:
        cnt+=1
print(cnt)