import sys

input = sys.stdin.readline


def find_number(start, end):
    res = 100000000
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        cur = 0
        for i in arr:
            if cnt > m:
                cnt += 1
                break
            elif cur + i > mid:
                cnt += 1
                cur = i
            else:
                cur += i
        if cnt <= m and max(arr) <= mid:
            res = min(res, mid)
        if cnt > m or max(arr) > mid:
            start = mid + 1
        else:
            end = mid - 1
    return res


n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = find_number(0, 100000000)
print(a)