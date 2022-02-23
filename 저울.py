import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
target = 1
for value in arr:
    if target < value:
        break
    target += value
print(target)
