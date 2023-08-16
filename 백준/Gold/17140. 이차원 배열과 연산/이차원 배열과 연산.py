from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import decimal
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline


r, c, k = map(int, input().split())
rNumber = 3
cNumber = 3
r -= 1
c -= 1


def R(y):
    global rNumber, cNumber
    tmpArr = []
    numberArr = []
    dic = {}
    for i in range(rNumber):
        curNumber = arr[i][y]
        if curNumber == 0:
            continue
        if curNumber in dic:
            dic[curNumber] += 1
        else:
            numberArr.append(curNumber)
            dic[curNumber] = 1
    numberArr.sort(key=lambda x: (dic[x], x))
    for i in range(len(numberArr)):
        tmpArr.append(numberArr[i])
        tmpArr.append(dic[numberArr[i]])
    for i in range(len(tmpArr)):
        if i == rNumber:
            rNumber += 1
            plusArr = [0 for j in range(cNumber)]
            arr.append(plusArr)
        arr[i][y] = tmpArr[i]
    for i in range(len(tmpArr), rNumber):
        arr[i][y] = 0


def C(x):
    global rNumber, cNumber
    tmpArr = []
    numberArr = []
    dic = {}
    for i in range(len(arr[x])):
        curNumber = arr[x][i]
        if curNumber == 0:
            continue
        if curNumber in dic:
            dic[curNumber] += 1
        else:
            numberArr.append(curNumber)
            dic[curNumber] = 1
    numberArr.sort(key=lambda x: (dic[x], x))
    for i in range(len(numberArr)):
        tmpArr.append(numberArr[i])
        tmpArr.append(dic[numberArr[i]])
    for i in range(len(tmpArr)):
        if i == len(arr[x]):
            arr[x].append(0)
            if i == cNumber:
                cNumber += 1
        arr[x][i] = tmpArr[i]
    for i in range(len(tmpArr), len(arr[x])):
        arr[x][i] = 0


arr = [[0 for i in range(3)] for i in range(3)]
for i in range(3):
    a = list(map(int, input().split()))
    for j in range(3):
        arr[i][j] = a[j]
time = 0
while time <= 100:
    if r < rNumber and c < cNumber:
        if arr[r][c] == k:
            break
    time += 1
    if rNumber >= cNumber:
        for i in range(rNumber):
            C(i)
        for i in range(rNumber):
            while len(arr[i]) < cNumber:
                arr[i].append(0)
    else:
        for i in range(cNumber):
            R(i)
    # for i in range(rNumber):
    #     print(arr[i])
    # print()
    if r < rNumber and c < cNumber:
        if arr[r][c] == k:
            break

if time > 100:
    print(-1)
    exit()
print(time)
