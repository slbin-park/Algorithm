import sys

input = sys.stdin.readline
a = input()
plus = 0
minus = 0
strnumber = ''
for i in range(len(a) - 1):
    if a[i] != '+' or a[i] != '-':
        strnumber += a[i]서

print(min(cnt1, cnt0))
