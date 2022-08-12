import sys

input = sys.stdin.readline

sum = 0

n = int(input())
arr = [[0, 0] for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    arr[i] = [a, b]
    sum += b

arr.sort()
mid = sum / 2
sum2 = 0
for i in range(n):
    sum2 += arr[i][1]
    if sum2 >= mid:
        print(arr[i][0])
        break
