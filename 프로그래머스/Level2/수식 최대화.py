from itertools import permutations


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def solution(expression):
    # isdigit
    answer = 0
    arr = []
    nxt = 0
    sign = []
    for i in range(len(expression)):
        if not expression[i].isdigit():  # 숫자가 아닐경우 앞에 숫자 , 기호를 넣어줌
            arr.append(expression[nxt:i])
            arr.append(expression[i])
            if expression[i] not in sign:
                sign.append(expression[i])
            nxt = i + 1
    arr.append(expression[nxt:len(expression)])  # 마지막 숫자를 배열에 넣어줌
    sign = list(permutations(sign, len(sign)))
    for i in range(len(sign)):
        arr2 = arr.copy()
        for j in sign[i]:
            stack = []
            while len(arr2) != 0:
                tmp = arr2.pop(0)
                if tmp == j:
                    stack.append(operation(stack.pop(), arr2.pop(0), j))
                else:
                    stack.append(tmp)
            arr2 = stack
        answer = max(answer, abs(int(arr2[0])))
    return answer
