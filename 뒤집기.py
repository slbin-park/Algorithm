import sys

input = sys.stdin.readline
a = input()
cnt1 = 0
cnt0 = 0
for i in range(len(a) - 1):
    if a[i] == '0' and a[i + 1] != '0':
        cnt0 += 1
    elif a[i] == '1' and a[i + 1] != '1':
        cnt1 += 1
print(min(cnt1, cnt0))
