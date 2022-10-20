import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
str1 = input().rstrip().split()
res = []
answer = []

def dfs(index):
    if index==n:
        answer.append(''.join(res))
    else:
        for i in range(10):
            if str1[index] == '>' and str(i) not in res:
                if int(res[index]) > i:
                    res.append(str(i))
                    dfs(index+1)
                    res.pop()
            else:
                if int(res[index]) < i and str(i) not in res:
                    res.append(str(i))
                    dfs(index+1)
                    res.pop()
for i in range(10):
    res.append(str(i))
    dfs(0)
    res.pop()
answer.sort(key=lambda x:int(x))
print(answer[-1])
print(answer[0])