import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
minus = []
plus = []
res = 0
for i in range(n):
    if arr[i] < 0:
        minus.append(arr[i])
    else:
        plus.append(arr[i])
minus.sort(reverse=True)
plus.sort()
renumber = 0
if len(minus) == 0:
    resnumber = max(plus)
elif len(plus) == 0:
    resnumber = -min(minus)
else:
    resnumber = max(max(plus), -min(minus))
while minus:
    for i in range(m):
        if len(minus) == 0:
            break
        if i == 0:
            res -= minus.pop() * 2
        else:
            minus.pop()
while plus:
    for i in range(m):
        if len(plus) == 0:
            break
        if i == 0:
            res += plus.pop() * 2
        else:
            plus.pop()
print(res - resnumber)
