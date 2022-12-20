import sys
import heapq
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
prev = 0
answer = 0
n = int(input())
n = 1000 - n
answer += n//500
n = n%500
answer += n//100
n = n%100
answer += n//50
n = n%50
answer += n//10
n = n%10
answer += n//5
n = n%5
answer += n//1
print(answer)
