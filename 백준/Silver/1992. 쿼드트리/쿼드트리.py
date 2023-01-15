import sys
import heapq
import math

input = sys.stdin.readline
INF = 1e9

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def dv(x, y, n):
    global answer
    flag = 0
    check = arr[x][y]
    for i in range(x, x + n):
        if flag == 1:
            break
        for j in range(y, y + n):
            if check != arr[i][j]:
                flag = 1
                break
    if flag:
        n = n // 2
        answer += "("
        dv(x, y, n)
        dv(x, y + n, n)
        dv(x + n, y, n)
        dv(x + n, y + n, n)
        answer += ")"
    else:
        answer += str(check)


answer = ""
n = int(input())
arr = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    a = input().strip()
    for j in range(n):
        arr[i][j] = a[j]
dv(0, 0, n)
print(answer)