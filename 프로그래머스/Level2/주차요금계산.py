from collections import defaultdict


def solution(fees, records):
    # fees = [기본시간 (분),기본 요금(원) , 단위 시간(분) , 단위 요금 (원)]
    dic = defaultdict(list)
    answer = []

    for i in range(len(records)):
        records[i] = records[i].split(' ')
        try:
            dic[records[i][1]].append((records[i][0], records[i][2]))
        except:
            dic[records[i][1]] = (records[i][0], records[i][2])

    dic = sorted(dic.items())

    for i in range(len(dic)):
        prev = ''
        res = 0
        time = 0
        for j in dic[i][1]:
            if j[1] == 'IN':
                prev = j[0]
            elif j[1] == 'OUT':
                prev = prev.split(':')
                cur = j[0].split(':')
                h = (int(cur[0]) - int(prev[0])) * 60
                m = int(cur[1]) - int(prev[1])
                time += h + m
                prev = ''
        #print(res)
        if prev != '':
            prev = prev.split(':')
            h = (23 - int(prev[0])) * 60
            m = 59 - int(prev[1])
            time += h + m
            #print('time = ',time)
        if time >= fees[0]:
            time = time - fees[0]
            if time % fees[2] == 0:
                res += fees[3] * (time // fees[2]) + fees[1]
            else:
                res += fees[3] * (time // fees[2] + 1) + fees[1]
        else:
            res += fees[1]
        #print(res)
        #print('----')
        answer.append(res)

    return answer