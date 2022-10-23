import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
str1 = input().rstrip()
res = []
answer = []
dic = {}
dic['B'] = 0
dic['R'] = 0
prev= str1[0]
dic[prev]+=1
for i in range(1,n):
    if prev!=str1[i]:
        dic[str1[i]]+=1
    prev = str1[i]

print(min(dic['B'],dic['R'])+1)