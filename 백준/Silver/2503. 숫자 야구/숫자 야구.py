import sys
import heapq
input = sys.stdin.readline
INF = 1e9


def dfs(depth):
    global cnt
    if depth==3:
        flag = 0
        for i in range(n):
            strike , ball = check(i)
            if arr[i][1] == strike and arr[i][2] == ball:
                flag = 0
            else:
                flag = 1
                break
        if flag == 0:
            cnt+=1
        return
    for i in range(1,10):
        if i not in bb:
            bb.append(i)
            dfs(depth+1)
            bb.pop()

def check(index):
    strike = 0
    ball = 0
    for i in range(3):
        a = str(arr[index][0])
        c = str(bb[i])
        if a[i] == c:
            strike +=1
        elif a.find(c) != -1:
            ball+=1
    return [strike,ball]
n = int(input())
cnt = 0
arr = []
bb = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dfs(0)
print(cnt)