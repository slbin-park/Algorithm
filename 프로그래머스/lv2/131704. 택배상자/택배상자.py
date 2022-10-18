def solution(order):
    stack =[]
    answer = 0
    index = 0
    for i in range(1,len(order)+1):
        if i == order[index]:
            index+=1
            answer+=1
            while len(stack) and stack[-1] == order[index]:
                index+=1
                answer+=1
                stack.pop()
        else:
            stack.append(i)
    while len(stack) and stack[-1] == order[index]:
        index+=1
        answer+=1
        stack.pop()
    return answer