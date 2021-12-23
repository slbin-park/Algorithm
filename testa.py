# 소스코드


def comp(n):

    c = n ^ 0b1111 + 1
    return bin(c)


print(comp(5))

# 출력결과

# 0b1011