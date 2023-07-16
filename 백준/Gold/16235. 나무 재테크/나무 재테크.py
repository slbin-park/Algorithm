from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
heap = []
die = []
n, m, k = map(int, input().split())
arr = [[5 for i in range(n)] for i in range(n)]
plus = [[0 for i in range(n)] for i in range(n)]
tree = [[deque() for i in range(n)] for i in range(n)]
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
for i in range(n):
    plus[i] = list(map(int, input().split()))
for i in range(m):
    r, c, age = map(int, input().split())
    tree[r - 1][c - 1].append(age)


def spring():
    global tree
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for k in range(len(tree[i][j])):
                    age = tree[i][j].popleft()
                    if arr[i][j] >= age:
                        arr[i][j] -= age
                        tree[i][j].append(age + 1)
                    else:
                        if age // 2 > 0:
                            die.append([i, j, age // 2])


def summer():
    global die
    for i in range(len(die)):
        arr[die[i][0]][die[i][1]] += die[i][2]
    die = []


def autumn():
    for i in range(n):
        for j in range(n):
            prev = []
            for age in tree[i][j]:
                if age % 5 == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].appendleft(1)


def winter():
    for i in range(n):
        for j in range(n):
            arr[i][j] += plus[i][j]


for i in range(k):
    spring()
    summer()
    autumn()
    winter()
res = 0
for i in range(n):
    for j in range(n):
        res += len(tree[i][j])
print(res)
