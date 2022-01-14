import sys

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
prevs = 1
prevl = m
sum = 0
for i in range(k):
    a = int(input())
    if a > prevl:
        sum += a - prevl
        prevl = a
        prevs = prevl - m + 1
    elif a < prevs:
        sum += prevs - a
        prevs = a
        prevl = a + m - 1
print(sum)
