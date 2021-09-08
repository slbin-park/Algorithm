import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()
cnt = 0
cntstr = 0
bc = len(b)
i = 0
while i <= len(a) - bc:
    if a[i:i + bc] == b:
        cnt += 1
        i = i + bc
    else:
        i += 1

print(cnt)
