def check(n):
    a = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            a += 1
    return True if (a + 1) % 2 == 0 else False


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if check(i) == True:
            answer += i
        else:
            answer -= i
    return answer