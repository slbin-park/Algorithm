import sys

input = sys.stdin.readline  #시작할때 해주면 좋음?
n = int(input())
a = [0 for i in range(10001)]
for i in range(n):
    a[int(input())] += 1
for i in range(10001):
    if a[i] > 0:
        for j in range(a[i]):
            print(i)
