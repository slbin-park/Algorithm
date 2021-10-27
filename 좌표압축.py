import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(arr)
res = {}
index = 0
for i in range(n):
    try:
        b = res[arr2[i]]
    except:
        res[arr2[i]] = index
        index += 1
for i in range(n):
    print(res[arr[i]], end=' ')
