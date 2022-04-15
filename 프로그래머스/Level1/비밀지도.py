def solution(n, arr1, arr2):
    answer = ['' for i in range(n)]
    map1 = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        map1_v = str(format(arr1[i], 'b'))
        map2_v = str(format(arr2[i], 'b'))
        map1_index = len(map1_v) - 1
        map2_index = len(map2_v) - 1
        for j in range(n - 1, -1, -1):
            if map1_index < 0:
                break
            else:
                if map1_v[map1_index] == '1':
                    map1[i][j] = 1
                map1_index -= 1
        for j in range(n - 1, -1, -1):
            if map2_index < 0:
                break
            else:
                if map2_v[map2_index] == '1':
                    map1[i][j] = 1
                map2_index -= 1
    for i in range(n):
        for j in range(n):
            if map1[i][j] == 1:
                answer[i] += '#'
            else:
                answer[i] += ' '
    print(answer)

    return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
