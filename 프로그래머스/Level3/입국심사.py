def solution(n, times):
    answer = 0
    left = 1
    right = max(times * n)
    maxn = right
    while left <= right:
        cnt = 0
        mid = (right + left) // 2
        for i in times:
            cnt += mid // i
        if cnt >= n:
            maxn = min(maxn, mid)
            right = mid - 1
        else:
            left = mid + 1
    return maxn