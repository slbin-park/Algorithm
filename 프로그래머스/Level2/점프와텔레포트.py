def solution(n):
    cnt = 0
    while n > 0:
        a = n // 2
        b = n % 2
        n = a
        if b != 0:
            cnt += 1
    return cnt