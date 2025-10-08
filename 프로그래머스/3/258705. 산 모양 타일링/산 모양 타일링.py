def solution(n, tops):
    answer = 0
    a1 = 0
    a2 = 0
    if tops[0] == 1:
        a1 = 3
        a2 = 1
    else:
        a1 = 2
        a2 = 1
    for i in range(1,len(tops)):
        if tops[i] == 0:
            prevA1 = a1
            a1 = a1 * 2 + a2
            a2 = prevA1 + a2
        else:
            prevA1 = a1
            a1 = a1 * 3 + a2 * 2
            a2 = prevA1 + a2
        # print(a1,a2)
    return (a1 + a2) % 10007