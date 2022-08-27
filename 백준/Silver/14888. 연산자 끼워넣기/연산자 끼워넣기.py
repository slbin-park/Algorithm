import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
input = sys.stdin.readline

def dfs(index,value , cur_plus , cur_minus , cur_mul , cur_div):
    global res_min , res_max
    if index == n-1:
        res_min = min(res_min,value)
        res_max = max(res_max,value)
        return
    if cur_plus <plus:
        dfs(index+1,value+arr[index+1],cur_plus+1,cur_minus,cur_mul,cur_div)
    if cur_minus < minus:
        dfs(index+1,value-arr[index+1],cur_plus,cur_minus+1,cur_mul,cur_div)
    if cur_mul < mul:
        dfs(index+1,value*arr[index+1],cur_plus,cur_minus,cur_mul+1,cur_div)
    if cur_div < div:
        if value==0:
            value =0
        elif value<0:
            tmp = -value // arr[index+1]
            value = -tmp
        else:value=value//arr[index+1]
        dfs(index+1,value,cur_plus,cur_minus,cur_mul,cur_div+1)

n = int(input())
arr = list(map(int,input().split()))

plus , minus , mul , div = map(int,input().split())
res_min = 1e9+1
res_max = -1e9-1
dfs(0,arr[0],0,0,0,0)
print(res_max)
print(res_min)