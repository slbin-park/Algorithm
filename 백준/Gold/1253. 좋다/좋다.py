from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys

sys.setrecursionlimit(10**5)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
dic = {}
for i in range(n):
    if arr[i] in dic:
        dic[arr[i]] += 1
    else:
        dic[arr[i]] = 1
res = 0
for i in range(n):
    left = 0
    right = n - 1
    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        else:
            if arr[right] + arr[left] == arr[i]:
                res += 1
                break
            elif arr[right] + arr[left] < arr[i]:
                left += 1
            else:
                right -= 1
print(res)
