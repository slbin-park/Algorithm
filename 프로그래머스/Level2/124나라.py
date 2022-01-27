def solution(n):
    strinp = ['4', '1', '2']
    answer = ''
    while n > 0:
        answer = strinp[n % 3] + answer
        if n % 3 == 0:
            n = n // 3 - 1
        else:
            n = n // 3
    return answer