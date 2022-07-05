import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    result = arr[0]
    for j in range(1,m):
        arr[j] = max(arr[j],arr[j]+arr[j-1])
        result = max(result,arr[j])
    print(result)