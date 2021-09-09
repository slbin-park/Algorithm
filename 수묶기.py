import sys

input = sys.stdin.readline
n = int(input())
parr = []
marr = []
res = 0
for i in range(n):
    a = int(input())
    if a == 1:
        res += 1
    elif a > 0:
        parr.append(a)
    else:
        marr.append(a)
parr.sort()
marr.sort(reverse=True)
while len(parr) != 0:
    if len(parr) == 1:
        res += parr.pop()
    else:
        res += parr.pop() * parr.pop()
while len(marr) != 0:
    if len(marr) == 1:
        res += marr.pop()
    else:
        res += marr.pop() * marr.pop()
print(res)
