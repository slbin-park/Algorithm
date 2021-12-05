triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
res = []
for i in range(len(triangle)):
    res.append(triangle[i])
print(res)

# 수정


def solution(triangle):
    arr = [[] for i in range(len(triangle))]
    for i in range(len(triangle)):
        for j in range(i + 1):
            arr[i].append(0)
    arr[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        arr[i][0] = arr[i - 1][0] + triangle[i][0]
        arr[i][i] = arr[i - 1][i - 1] + triangle[i][i - 1]
        for j in range(1, i):
            arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + triangle[i][j]
    print(arr)

    answer = 0
    return answer


print(solution(triangle))