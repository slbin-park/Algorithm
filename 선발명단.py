import sys

sys.setrecursionlimit(10**8)


def find_res(number, cur):
    global res
    if number == 11:
        res = max(res, cur)
        return
    for i in range(11):
        if arr[number][i] != 0 and sel[i] == 0:
            sel[i] = 1
            find_res(number + 1, cur + arr[number][i])
            sel[i] = 0


n = int(input())
for j in range(n):
    sel = [0 for i in range(11)]
    arr = []
    res = 0
    for k in range(11):
        arr.append(list(map(int, input().split())))
    find_res(0, 0)
    print(res)