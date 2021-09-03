n = int(input())
arr = [[0] * 10 for i in range(n + 1)]
arr[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n + 1):
    for j in range(10):
        arr[i][j] = sum(arr[i - 1][j:10]) % 10007
print(sum(arr[n]) % 10007)
