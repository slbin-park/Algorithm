import sys

input = sys.stdin.readline

n = int(input())
arr = [[] for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    arr[i] = [a, b]
arr.sort(key=lambda x: x[0])
res = [0 for i in range(1001)]
for i in range(n):
    flag = 0
    flag2 = 0
    minindex = 0
    minum = arr[i][1]
    for j in range(arr[i][0]):
        if res[j] == 0:
            res[j] = arr[i][1]
            flag = 1
            break
    if flag == 0:
        for j in range(arr[i][0]):
            if minum > res[j]:
                minum = res[j]
                minindex = j
                flag2 = 1
    if flag2 == 1:
        res[minindex] = arr[i][1]
print(sum(res))