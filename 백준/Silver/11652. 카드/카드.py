import sys
import heapq

input = sys.stdin.readline
n = int(input())
dic = {}
for i in range(n):
    a = int(input())
    try:
        dic[a] += 1
    except:
        dic[a] = 1
a = [0, 0]
for i in dic:
    if dic[i] > a[0]:
        a = [dic[i], i]
    elif dic[i] == a[0]:
        if i < a[1]:
            a = [dic[i], i]
print(a[1])