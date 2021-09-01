import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
result =[0 for _ in range(n+1)]
arr.sort()
result[0] = arr[0]

for i in range(1,n):
    result[i] = arr[i]+result[i-1]
res = 0
for i in range(n):
    res +=result[i]
print(res)