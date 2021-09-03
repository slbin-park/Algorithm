import sys

input = sys.stdin.readline

n = int(input())
res = 0
cnt = 0
while res != n:
    if res + 3 <= n:
        res += 3
        cnt += 1
    else:
        res += 1
        cnt += 1
if cnt % 2 == 1:
    print('SK')
else:
    print('CY')
