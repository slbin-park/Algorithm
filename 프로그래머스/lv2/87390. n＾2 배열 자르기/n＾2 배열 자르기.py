def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = 0
        if i+1>n:
            a = i//n+1
        if i%n+1 > a:
            a = i%n+1
        answer.append(a)
    # 123
    # 223
    # 333
    # 4444
    return answer