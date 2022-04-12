def check(str1):
    stack = []
    for i in str1:
        if len(stack) != 0:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '{' and i == '}':
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    return True if len(stack) == 0 else False


def solution(s):
    answer = 0
    if check(s) == True:
        answer += 1
    for i in range(len(s) - 1):
        s = s[1:len(s)] + s[0]
        if check(s) == True:
            answer += 1
    return answer