n = int(input())
arr = [[0 for _ in range(3)] for i in range(n + 1)]
arr[1][0] = 1
arr[1][1] = 1
arr[1][2] = 1
for i in range(2, n + 1):
    arr[i][0] = arr[i - 1][1] + arr[i - 1][2] % 9901
    arr[i][1] = arr[i - 1][0] + arr[i - 1][2] % 9901
    arr[i][2] = arr[i - 1][0] + arr[i - 1][1] + arr[i - 1][2] % 9901
print(sum(arr[n]) % 9901)
