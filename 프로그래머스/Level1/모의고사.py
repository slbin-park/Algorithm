def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p1_res = 0
    p2_res = 0
    p3_res = 0
    for i in range(len(answers)):
        p1_res += 1 if p1[(i % len(p1))] == answers[i] else 0
        p2_res += 1 if p2[(i % len(p2))] == answers[i] else 0
        p3_res += 1 if p3[(i % len(p3))] == answers[i] else 0
    a = max(p1_res, p2_res, p3_res)
    if a == p1_res:
        answer.append(1)
    if a == p2_res:
        answer.append(2)
    if a == p3_res:
        answer.append(3)
    return answer
