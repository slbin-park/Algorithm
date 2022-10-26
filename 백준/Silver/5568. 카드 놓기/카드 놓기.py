import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
k = int(input())
arr = [int(input())for i in range(n)]
dic = set()
prev_arr = []
vis = [0 for i in range(n)]
def get_num():
    if len(prev_arr) == k:
        dic.add(int(''.join(prev_arr)))
    for i in range(n):
        if vis[i] == 0:
            vis[i] = 1
            prev_arr.append(str(arr[i]))
            get_num()
            vis[i] = 0
            prev_arr.pop()
            
get_num()
print(len(dic))