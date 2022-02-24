from collections import defaultdict


def solution(id_list, report, k):
    dic = defaultdict(list)
    legn = len(id_list)
    arr = [[0 for i in range(legn)] for i in range(legn)]
    answer = [0 for i in range(legn)]
    res = [0 for _ in range(legn)]

    for i in range(legn):
        dic[id_list[i]] = i
    for name in report:
        name = name.split(' ')
        if arr[dic[name[0]]][dic[name[1]]] < 1:
            arr[dic[name[0]]][dic[name[1]]] += 1
            res[dic[name[1]]] += 1

    for i in range(legn):
        for j in range(legn):
            if arr[i][j] > 0 and res[j] >= k:
                answer[i] += 1

    return answer