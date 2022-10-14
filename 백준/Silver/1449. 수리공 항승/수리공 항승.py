import sys
input = sys.stdin.readline
n,m  = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
cnt = 1
prev = arr[0]
for i in range(1,n):
    if arr[i]-prev >= m:
        cnt+=1
        prev = arr[i]
print(cnt)