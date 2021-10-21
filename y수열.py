import sys


def dcy():
    start = 0
    flag = 0
    for i in range(n - 1):
        if arr[i] >= arr[i + 1]:
            if i == n - 2:
                flag = 2
                start = -1
        else:
            start = i
            break
    if start != -1:
        for i in range(start + 1, n - 1):
            if arr[i] >= arr[i + 1]:
                continue
            else:
                flag = 1
                break
    if flag == 1:
        return -1
    elif flag == 2:
        return 0
    elif arr[0] <= arr[n - 1]:
        return start + 1


def icy():
    start = 0
    flag = 0
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            if i == n - 2:
                flag = 2
                start = -1
            continue
        else:
            start = i
            break
    if start != -1:
        for i in range(start + 1, n - 1):
            if arr[i] <= arr[i + 1]:
                continue
            else:
                flag = 1
                break
    if flag == 1:
        return -1
    elif flag == 2:
        return 0
    elif arr[0] >= arr[n - 1]:
        return start + 1


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
if arr[0] > arr[1]:
    print(dcy())
else:
    print(icy())