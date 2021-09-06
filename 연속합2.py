import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [[] for i in range(n)]
maxres = 0
if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[1], arr[0], arr[0] + arr[1]))
elif n >= 3:
    res[0] = arr[0]
    res[1] = max(res[0] + arr[1], arr[1])
    res[2] = max(res[1] + arr[2], arr[2], arr[1] + arr[2])
    for i in range(3, n):
        res[i] = max(res[i - 1] + arr[i], arr[i], arr[i - 1] + arr[i])
    maxres = max(res)
    resnum = res[0]
    check = 0
    for i in range(1, n):
        if check == 0:
            if res[i] > res[i - 1]:
                maxres = res[i]
                resnum = max(maxres, resnum)
            else:
                maxres = res[i - 1]
                resnum = max(maxres, resnum)
                check = 1
        else:
            if maxres > maxres + arr[i]:
                if res[i] < res[i - 1]:
                    maxres = res[i - 1]
                    resnum = max(maxres, resnum)
                else:
                    maxres = res[i]
                    resnum = max(maxres, resnum)
                    check = 0
            else:
                maxres += arr[i]
                resnum = max(maxres, resnum)
    print(resnum)
