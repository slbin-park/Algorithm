def solution(progresses, speeds):
    answer = []
    while progresses:
        res = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while len(progresses) > 0 and progresses[0] > 99:
            res += 1
            progresses.pop(0)
            speeds.pop(0)
        if res != 0:
            answer.append(res)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
