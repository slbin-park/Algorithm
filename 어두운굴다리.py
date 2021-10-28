import sys


def bisearch(start, end):
    global res
    while start <= end:
        prev = 0
        mid = (start + end) // 2
        for i in range(m - 1):
            if prev < arr[i] - mid:
                start = mid + 1
                break
            prev = arr[i] + mid
        if arr[m - 1] - mid > prev or arr[m - 1] + mid < n:
            start = mid + 1
        else:
            end = mid - 1
            res = mid


input = sys.stdin.readline
n = int(input())
m = int(input())
res = 0
arr = list(map(int, input().split()))
bisearch(0, 100000)
if m == 1:
    print(n)
else:
    print(res)
