import sys

INF = 10000000000

n = int(input())
arr = list(map(int, input().split()))
left = 0
right = n - 1
res = [0, 0]
max_n = INF
while left < right:
    cur_value = arr[left] + arr[right]
    if max_n > abs(cur_value):
        res = [left, right]
        max_n = abs(cur_value)
    if cur_value < 0:
        left += 1
    else:
        right -= 1
print(arr[res[0]], arr[res[1]])
