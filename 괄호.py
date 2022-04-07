import sys


def check(a):
    stack = []
    for i in range(len(a)):
        if len(stack) == 0:
            stack.append(a[i])
        else:
            if stack[-1] == '(' and a[i] == ')':
                stack.pop()
            else:
                stack.append(a[i])
    return True if len(stack) == 0 else False


input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = input().strip()
    if check(a) == True:
        print('YES')

    else:
        print('NO')
