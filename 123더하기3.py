import sys

n = int(input())
arr = [0 for j in range(1000001)]
arr[0] = 1
arr[1] = 1
arr[2] = 2
for i in range(3, 1000001):
    arr[i] = arr[i - 1] % 1000000009 + arr[i - 2] % 1000000009 + arr[
        i - 3] % 1000000009
for i in range(n):
    a = int(input())
    print(arr[a] % 1000000009)
