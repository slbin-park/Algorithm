n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
res = 0
print(arr)
for i in range(n // 2):
    res += arr[i] - arr[-i - 1]
    print(arr[i], arr[-i - 1])
    print(res)
print(res)