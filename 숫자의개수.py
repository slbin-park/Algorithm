import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
res = a*b*c
arr = [0 for i in range(10)]
for i in str(res):
    arr[int(i)] += 1
for i in arr:
    print(i)
