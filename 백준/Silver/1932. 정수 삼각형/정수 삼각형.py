n = int(input())
arr = []
arr.append([int(input())])
dp = [arr[0][0]]
if n > 1:
    for i in range(1, n):
        arr.append(list(map(int, input().split())))
        for j in range(i + 1):
            if j == 0:
                arr[i][j] += arr[i - 1][j]
            elif i == j:
                arr[i][j] += arr[i - 1][j - 1]
            else:
                arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

print(max(arr[n - 1]))
