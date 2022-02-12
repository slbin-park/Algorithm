def solution(n, words):
    answer = []
    stack = []
    res = 0
    flag = 0
    for i in range(len(words)):
        if words[i] in stack:
            res = i
            flag = 1
            break
        if i > 0:
            if words[i - 1][-1] != words[i][0]:
                res = i
                flag = 1
                break
        stack.append(words[i])
    if flag == 0:
        return [0, 0]
    res += 1
    person = n if res % n == 0 else res % n
    lst = res // n + 1 if res % n > 0 else res // n

    return [person, lst]
