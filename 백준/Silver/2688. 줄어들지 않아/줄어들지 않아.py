import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(66)]
arr[2] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
res = [0 for i in range(66)]
res[2] = sum(arr[2])
res[1] = 10
for i in range(3, 65):
    for j in range(10):
        arr[i][j] = sum(arr[i - 1][j:10])
    res[i] = sum(arr[i])
for i in range(n):
    a = int(input())
    print(res[a])
