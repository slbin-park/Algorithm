def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    prev = routes[0][1]
    for i in range(1, len(routes)):
        if prev < routes[i][0]:
            answer += 1
            prev = routes[i][1]
        elif prev > routes[i][1]:
            answer += 1
            prev = routes[i][1]
    return answer