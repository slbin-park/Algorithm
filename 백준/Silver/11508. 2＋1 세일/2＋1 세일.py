import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
answer = 0
for i in range(n):
    if (i % 3 != 2):
        answer += arr[i]
print(answer)