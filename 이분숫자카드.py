import sys

input = sys.stdin.readline


def bisearch(s, e, f):
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == f:
            return 1
        elif arr[mid] < f:
            s = mid + 1
        else:
            e = mid - 1
    return 0


n = int(input())
arr = list(map(int, input().split()))
start = 0
end = n - 1
m = int(input())
arr2 = list(map(int, input().split()))
arr.sort()
for i in range(m):
    print(bisearch(start, end, arr2[i]), end=' ')
