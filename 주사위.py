import sys

input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
if n == 1:
    print(sum(arr1) - max(arr1))
else:
    arr = [min(arr1[0], arr1[5]), min(arr1[1], arr1[4]), min(arr1[2], arr1[3])]
    arr.sort()
    res0 = (arr[0] + arr[1]) * (n - 1) * 4
    res1 = (arr[0] + arr[1]) * (n - 2) * 4
    res2 = (arr[0] + arr[1] + arr[2]) * 4
    res3 = (arr[0]) * (n - 2) * 4
    res4 = arr[0] * (n - 2) * (n - 2) * 5
    print(res0 + res1 + res2 + res3 + res4)
