import sys

input = sys.stdin.readline


def boom(ans, res):
    stack = []
    index = 0
    for i in range(len(ans)):
        stack.append(ans[i])
        if len(stack) >= len(res):
            if str(ans[i]) == str(res[len(res) - 1]) and ''.join(
                    stack[index - len(res) + 1:index + 1]) == res:
                for i in range(len(res)):
                    stack.pop()
                    index -= 1
        index += 1
    return stack


n = input().strip()
m = input().strip()
res = ''.join(boom(n, m))
if res == '':
    print('FRULA')
else:
    print(res)
