def solution(edges):
    answer = [0,0,0,0]
    n = 0
    for a,b in edges:
        n = max(a,n)
        n = max(b,n)
    arr = [[0,0] for i in range(n+1)]
    for o,i in edges:
        arr[o][1] += 1
        arr[i][0] += 1
    # 0 = 진입 개수
    # 1 = 외부 나가는 개수
    # print(arr[1:])
    cnt = 0
    for i in range(1,n+1):
        if arr[i][0] == 0:
            if cnt < arr[i][1]:
                answer[0] = i
                cnt = arr[i][1]
        elif arr[i][1] == 0:
            answer[2] += 1
        elif (arr[i][0] + arr[i][1]) >= 4:
            answer[3] += 1
    answer[1] = cnt - answer[3] - answer[2]
    # 1: 도넛
    # 2: 막대
    # 3: 팔자
    return answer