import sys

input = sys.stdin.readline
str = input().strip()
res = []
for i in range(len(str) - 1, -1, -1):
    res.append(str[i:len(str)])
res.sort()
for i in range(len(str)):
    print(res[i])