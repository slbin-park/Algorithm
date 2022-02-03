def solution(s):
    answer = 1
    stack = []
    for i in s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return 0

    return answer