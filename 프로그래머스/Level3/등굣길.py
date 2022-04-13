def solution(m, n, puddles):
    answer = 0
    arr = [[0 for i in range(m + 1)] for _ in range(n + 1)]
    arr[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:
                continue
            else:
                if i + 1 < n + 1 and [j, i + 1] not in puddles:
                    arr[i + 1][j] += arr[i][j] % 1000000007
                if j + 1 < m + 1 and [j + 1, i] not in puddles:
                    arr[i][j + 1] += arr[i][j] % 1000000007
    return arr[-1][-1] % 1000000007
