from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
input = sys.stdin.readline

def dfs(index):
    # print(arr[index][1] == index)
    global result
    result.append(index)
    if arr[index][1] == index:
        return
    else:
        dfs(arr[index][1])
n = int(input())
arr = [[1e9,0] for i in range(n+1)]
result = []
arr[n] = [0,n]
for i in range(n,0,-1):
    cur_cnt = arr[i][0]+1
    if i%3 == 0:
        tmp = i//3
        if arr[tmp][0] > cur_cnt:
            arr[tmp][0] = cur_cnt
            arr[tmp][1] = i
    if i%2 == 0:
        tmp = i//2
        if arr[tmp][0] > cur_cnt:
            arr[tmp][0] = cur_cnt
            arr[tmp][1] = i
    tmp = i-1
    if arr[tmp][0] > cur_cnt:
        arr[tmp][0] = cur_cnt
        arr[tmp][1] = i
dfs(1)
print(arr[1][0])
print(*result[::-1])
# for i in range(len(result)-1,0,-1):
#     print(result[i],end=' ')
# print(result[0],end='')