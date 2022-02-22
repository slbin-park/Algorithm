import string


def convert(num, base):
    tmp = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    answer = ''
    cnt = t * m
    turn = 1
    res = ''
    for i in range(cnt):
        res += convert(i, n)
    cur = 0
    for i in range(len(res)):
        if len(answer) == t:
            break
        if turn == p:
            answer += res[i]
        turn += 1
        if turn > m:
            turn = 1
        cur += 1
    return answer