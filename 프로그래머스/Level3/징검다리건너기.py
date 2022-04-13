def solution(stones, k):
    answer = 0
    start = 1
    end = max(stones)
    while start <= end:
        mid = (start + end) // 2
        cur = 0
        for stone in stones:
            if stone - mid <= 0:
                cur += 1
            else:
                cur = 0
            if cur >= k:
                break
        if cur < k:
            start += 1
        else:
            end -= 1
            answer = mid
    return answer
