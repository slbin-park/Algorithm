import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = input().strip()
    m = int(input())
    flag = 1
    arr = input().strip()
    arr = arr.replace("[", "")
    arr = arr.replace("]", "")
    arr = arr.split(',')
    dq = deque(arr)
    if len(arr) == 1:
        dq = deque()
    arr = []
    for i in range(len(a)):
        if a[i] == 'R':
            for i in range(len(dq)):
                arr.append(dq.pop())
            dq = deque(arr)
            arr = []
        elif a[i] == 'D':
            if len(dq) == 0:
                print('error')
                flag = 0
                break
            else:
                dq.popleft()
    if flag == 0:
        continue
    else:
        print('[', end='')
        for i in dq:
            if i == dq[-1]:
                print(i, end='')
            else:
                print(i, end=',')
        print(']')
