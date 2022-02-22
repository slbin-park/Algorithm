def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == ')':
            try:
                if stack[-1] == '(':
                    stack.pop()
            except:
                return False
        else:
            stack.append(s[i])
    if len(stack) > 0:
        return False

    return True