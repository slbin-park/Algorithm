import collections


def solution(record):
    dic = collections.defaultdict(list)
    res = []
    answer = []
    for i in range(len(record)):
        arr = record[i].split(' ')
        if arr[0] == 'Enter':
            dic[arr[1]] = arr[2]
            res.append([arr[0], arr[1]])
        elif arr[0] == 'Leave':
            res.append([arr[0], arr[1]])
        elif arr[0] == 'Change':
            dic[arr[1]] = arr[2]
    for i in range(len(res)):
        if res[i][0] == 'Enter':
            answer.append(dic[res[i][1]] + '님이 들어왔습니다.')
        elif res[i][0] == 'Leave':
            answer.append(dic[res[i][1]] + '님이 나갔습니다.')
    return answer