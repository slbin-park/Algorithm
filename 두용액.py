import sys

input = sys.stdin.readline


def bisearch(start, end):
    global s1, s2, res
    while start <= end:
        if abs(arr[start] + arr[end]) < res:
            s1 = arr[start]
            s2 = arr[end]
            res = abs(arr[start] + arr[end])
        if arr[start] + arr[end] < 0:
            start += 1
        else:
            end -= 1


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 2e+9 + 1
s1 = 0
s2 = 0
bisearch(0, n - 1)
print(s1, s2)
