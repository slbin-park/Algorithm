def solution(n):
    answer = 0
    for i in range(2,n):
        if n%i==1:
            return i
    return answer