import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(0)
    exit(0)
arr.sort()
res = 1e9
cur = 0

for i in range(1, len(arr)):
    cur += arr[i] - arr[0]
res = cur
number = arr[0]
for i in range(1, len(arr)):
    cur = cur + (arr[i] - arr[i - 1]) * (i) - (arr[i] -
                                               arr[i - 1]) * (len(arr) - i)
    if cur < res:
        res = cur
        number = arr[i]
print(number)

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# # 중간값 (medium)을 출력
# print(data[(n - 1) // 2])
