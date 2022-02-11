def solution(rows, columns, queries):
    answer = []
    arr = [[0 for col in range(columns)] for row in range(rows)]

    val = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = val
            val += 1
    for x1, y1, x2, y2 in queries:
        prev = arr[x1 - 1][y1 - 1]
        minn = prev
        for i in range(y1 - 1, y2):
            tmp = arr[x1 - 1][i]
            minn = min(tmp, minn)
            arr[x1 - 1][i] = prev
            prev = tmp

        for i in range(x1, x2):
            tmp = arr[i][y2 - 1]
            minn = min(tmp, minn)
            arr[i][y2 - 1] = prev
            prev = tmp

        for i in range(y2 - 2, y1 - 2, -1):
            tmp = arr[x2 - 1][i]
            minn = min(tmp, minn)
            arr[x2 - 1][i] = prev
            prev = tmp

        for i in range(x2 - 2, x1 - 2, -1):
            tmp = arr[i][y1 - 1]
            minn = min(tmp, minn)
            arr[i][y1 - 1] = prev
            prev = tmp

        answer.append(minn)

    return answer


rows = 2
columns = 9
queries = [[1, 1, 2, 2]]
print(solution(rows, columns, queries))
