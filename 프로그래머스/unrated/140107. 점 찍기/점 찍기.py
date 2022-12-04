import math
def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        a = math.sqrt(d**2 - i**2)
        answer += a//k +1
    return answer