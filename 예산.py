import sys

input = sys.stdin.readline


def find_number(start, end):
    while start <= end:
        cur = 0
        mid = (start + end) // 2
        for i in arr:
            if i > mid:
                cur += mid
            else:
                cur += i
        if cur <= m:
            start = mid + 1
        else:
            end = mid - 1
    return end


n = int(input())
arr = list(map(int, input().split()))
m = int(input())
a = find_number(0, max(arr))
print(a)
