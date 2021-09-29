import sys

n = int(input())
arr = list(map(int, input().split()))
res = 0
arr.sort()
while len(arr) != 1:
    a = arr.pop()
    b = arr.pop()
    res += a * b
    arr.append(a + b)
print(res)