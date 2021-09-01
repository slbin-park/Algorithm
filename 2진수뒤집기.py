from collections import deque
n = int(input())
a = format(n, 'b')
b = ''
dq = deque()
res = 0
cnt = 0
for i in str(a):
    dq.append(i)
    cnt += 1
for i in range(cnt):
    b = dq.popleft()
    if b == '1':
        res += 2**int(i)

print(res)
