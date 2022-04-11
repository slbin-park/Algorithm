from string import ascii_uppercase


def solution(msg):
    answer = []
    alp = list(ascii_uppercase)
    dic = {}

    for i in range(len(alp)):
        dic[alp[i]] = i + 1
    maxn = 1  # 최대 사전 길이
    nxt = 27  # 사전 다음 번호
    i = 0  # 현재 인덱스
    while i < len(msg):
        flag = 0
        print('i = ', i)
        for j in range(maxn + 1, 1, -1):
            try:
                answer.append(dic[msg[i:i + j]])
                dic[msg[i:i + j + 1]] = nxt
                print('사전추가')
                print(msg[i:i + j + 1])
                print(nxt)
                maxn = max(maxn, j)
                i += j
                nxt += 1
                flag = 1
                break
            except:
                continue
        if i == len(msg) - 1:
            answer.append(dic[msg[i]])
            break

        if flag == 0:
            dic[msg[i:i + 2]] = nxt
            print('밑에서 사전추가')
            print(msg[i:i + 2])
            print(nxt)
            nxt += 1
            answer.append(dic[msg[i]])
            i += 1
    print(answer)
    return answer


solution('TOBEORNOTTOBEORTOBEORNOT')