import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
res = [1 for i in range(n)]
for i in range(n):
    a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    if a >= b:
        res[i] = arr[a-b]
res.sort()
cnt = 0
answer = 0
for i in range(n):
    if answer+res[i] <= m:
        cnt+=1
        answer+=res[i]
    else:
        break;
print(cnt)