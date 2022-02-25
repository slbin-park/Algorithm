from collections import deque


def dfs(n, info):
    init = [0 for i in range(11)]
    dq = deque()
    dq.append((0, init))
    res = 0
    answer = []
    while dq:
        idx, score = dq.popleft()

        if sum(score) > n:
            continue
        elif sum(score) == n:
            apeach = 0
            lion = 0
            for i in range(11):
                if not (info[i] == 0 and score[i] == 0):
                    if info[i] < score[i]:
                        apeach += 10 - i
                    elif info[i] > score[i]:
                        lion += 10 - i
            if apeach > lion:
                if res > apeach - lion:
                    continue
                if res < apeach - lion:
                    res = apeach - lion
                    answer.clear()
                answer.append(score)
        elif idx == 10:
            tmp = score.copy()
            tmp[idx] = n - sum(tmp)
            dq.append((11, tmp))
            continue
        else:
            tmp = score.copy()
            dq.append((idx + 1, tmp))
            tmp2 = score.copy()
            tmp2[idx] = info[idx] + 1
            dq.append((idx + 1, tmp2))
    return answer


def solution(n, info):
    answer = []
    arr = dfs(n, info)
    print(arr)
    if len(arr) == 0:
        return [-1]
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[-1]
    return answer