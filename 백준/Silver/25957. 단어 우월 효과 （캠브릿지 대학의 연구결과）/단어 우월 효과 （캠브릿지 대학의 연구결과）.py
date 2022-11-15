import sys
import heapq
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
dic = {}
n = int(input())
for i in range(n):
    str1 = input().rstrip()
    c_arr = []
    for j in range(len(str1)):
        c_arr.append(str1[j])
    c_arr.sort()
    c_arr.append(str1[0])
    c_arr.append(str1[-1])
    dic["".join(c_arr)] = str1
m = int(input())
arr = input().rstrip().split(" ")
for i in range(m):
    str1 = arr[i]
    c_arr = []
    for j in range(len(str1)):
        c_arr.append(str1[j])
    c_arr.sort()
    c_arr.append(str1[0])
    c_arr.append(str1[-1])
    if i == m-1:
        print(dic["".join(c_arr)])
        break;
    print(dic["".join(c_arr)],end=" ")