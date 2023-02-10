import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0
for i in range(n):
    for j in range(arr[i]):
        cnt+=1
        if n-2 == cnt and j==arr[i]-1:
            print(cnt)
            exit(0)
        elif n-1 == cnt:
            print(cnt)
            exit(0)
    n-=1
print(cnt)