import sys

from itertools import combinations

input = sys.stdin.readline

n = int(input())
for i in range(n):
    a = int(input())
    dic = {}
    for j in range(a):
        a, b = input().split()
        try:
            dic[b] += 1
        except:
            dic[b] = 1
    res = 1
    cur = 0
    for item in dic:
        res *= dic[item] + 1
    res = res - 1
    print(res)