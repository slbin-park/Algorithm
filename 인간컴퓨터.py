import sys

input = sys.stdin.readline

name = input().strip()
n = int(input())
for i in range(n):
    a = input().split()
    sum = 0
    for j in range(int(a[1]), int(a[2]) + 1):
        if name[j] == a[0]:
            sum += 1
    print(sum)