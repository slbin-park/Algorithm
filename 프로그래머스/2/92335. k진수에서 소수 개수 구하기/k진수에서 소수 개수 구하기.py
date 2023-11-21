import math
def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    tmp = ''
    while n:
        tmp = str(n % k) + tmp
        n = n // k
    tmp = tmp.split("0")
    # print(tmp)
    for i in range(len(tmp)):
        if tmp[i]!='' and tmp[i] != '1':
            # print(tmp[i])
            if is_prime_num(int(tmp[i])):
                answer+=1
    return answer