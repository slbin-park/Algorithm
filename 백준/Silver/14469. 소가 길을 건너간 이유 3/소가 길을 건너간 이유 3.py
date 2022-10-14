import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
arr.sort(key=lambda x:x[0])
time = 0
for i in range(n):
    time = max(time,arr[i][0])
    time+=arr[i][1]
print(time)