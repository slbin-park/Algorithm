import sys

input = sys.stdin.readline


def bisearch(start, end):
    global ans
    while start <= end:
        mid = (start + end) // 2
        res = 0
        flag = 0
        for i in range(n):
            res += mid // arr[i]
            if res >= m:
                flag = 1
                break
        if flag == 1:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1


n, m = map(int, input().split())
ans = 0
arr = list(map(int, input().split()))
arr.sort()
bisearch(1, 1000000000001)
print(ans)