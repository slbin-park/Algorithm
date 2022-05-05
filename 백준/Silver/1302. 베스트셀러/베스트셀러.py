import sys
import heapq

input = sys.stdin.readline
n = int(input())
dic = {}
for i in range(n):
    a = input().strip()
    try:
        dic[a] += 1
    except:
        dic[a] = 1
a = 0
res = []
for i in dic:
    if dic[i] > a:
        a = dic[i]
        res = [i]
    elif dic[i] == a:
        res.append(i)
res.sort()
print(res[0])
