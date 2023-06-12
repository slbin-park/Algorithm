import sys
import heapq
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
m = int(input())
str1 = input().strip()
cmp = 'I'
cmp_num = 1+(2*n)
res = 0
for i in range(n):
    cmp +='OI'
for i in range(m):
    if str1[i:i+cmp_num] == cmp:
        res+=1
print(res)