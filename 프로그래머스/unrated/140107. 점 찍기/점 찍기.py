import math
def solution(k, d):
    return sum([math.sqrt(d**2-i**2)//k+1 for i in range(0,d+1,k)])