import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def change(p_arr):
    return p_arr[1:]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x
def union(x,y):
    x = find(x)
    y = find(y)
    if x > y:
        tmp = x
        x = y
        y = tmp
    if x!=y:
        parent[y] = x
n,m = map(int,input().split())
truth = list(map(int,input().split()))
parent = [i for i in range(n+1)]

# parent를 젤 낮은숫자로 변경
if truth[0] > 0 :
    truth = change(truth)
    truth.sort()
    for i in range(1,len(truth)):
        parent[truth[i]] = truth[0]
arr = []
for i in range(m):
    a = list(map(int,input().split()))
    a = change(a)
    arr.append(a)
    a.sort()
    cur_parent = find(a[0])
    for j in range(1,len(a)):
        union(parent[a[j]],a[0])
res = 0
for i in range(m):
    a = find(parent[truth[0]])
    flag = 1
    for j in range(len(arr[i])):
        if a == find(parent[arr[i][j]]):
            flag = 0
            break;
    if flag==1:
        res+=1
print(res)