import collections


def solution(n, k, cmd):
    # k 는 현재위치
    # cmd 는 명령어들 모임
    res = collections.defaultdict(list)
    res[0] = [-1, 1]
    res[n - 1] = [n - 2, -1]
    start = 0
    for i in range(1, n - 1):
        res[i] = [i - 1, i + 1]
    prevdel = []
    for i in range(len(cmd)):
        a = cmd[i].split(' ')
        if a[0] == 'D':
            for i in range(int(a[1])):
                k = res[k][1]
        if a[0] == 'U':
            for i in range(int(a[1])):
                k = res[k][0]
        if a[0] == 'C':  # 삭제
            prevdel.append(k)
            if res[k][1] == -1:  # 마지막이면 앞에꺼만 -1로 바꿈
                res[res[k][0]][1] = -1
                k = res[k][0]
            elif res[k][0] == -1:
                res[res[k][1]][0] = -1
                k = res[k][1]
                start = k
            else:  # 아닐경우 앞 뒤로 연결해줌
                res[res[k][0]][1] = res[k][1]  # 앞에꺼랑 뒤에꺼 연결
                res[res[k][1]][0] = res[k][0]  # 뒤에꺼랑 앞에꺼 연결
                k = res[k][1]
        if a[0] == 'Z':  # 되돌리기
            if len(prevdel) != 0:
                c = prevdel.pop()
                if res[c][1] == -1:
                    res[res[c][0]][1] = c
                elif res[c][0] == -1:
                    res[res[c][1]][0] = c
                    start = c
                else:
                    res[res[c][0]][1] = c  # 앞에꺼라 삭제됐던거 연결
                    res[res[c][1]][0] = c  # 뒤에꺼랑 삭제됐던거 연결
    answer = ''
    ans = []
    ans.append(start)
    arr = collections.defaultdict(list)
    for i in range(n):
        arr[i] = 0
    while ans:
        c = ans.pop()
        if c != -1:
            arr[c] = 1
            ans.append(res[c][1])
    for i in range(n):
        if arr[i] == 1:
            answer += 'O'
            c += 1
        else:
            answer += 'X'
    return answer