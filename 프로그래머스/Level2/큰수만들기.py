def solution(number, k):
    answer = ''
    stack = []
    if k == 0:
        return number
    for i in range(len(number)):
        if k == 0:
            for j in range(i, len(number)):
                stack.append(int(number[j]))
            break
        if len(stack) == 0:
            stack.append(int(number[i]))
            continue
        elif int(stack[-1]) < int(number[i]):
            while k != 0 and len(stack) != 0 and int(stack[-1]) < int(
                    number[i]):
                stack.pop()
                k -= 1
        stack.append(int(number[i]))
    for i in range(len(stack) - k):
        answer += str(stack[i])
    return answer