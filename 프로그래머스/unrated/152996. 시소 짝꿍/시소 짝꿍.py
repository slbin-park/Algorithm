def solution(weights):
    answer = 0
    arr = [0 for i in range(4001)]
    vis = [0 for i in range(1001)]
    for i in weights:
        a2 = i*2
        a3 = i*3
        a4 = i*4
        answer += arr[a2]
        answer += arr[a3]
        answer += arr[a4]
        if vis[i] >0:
            answer -= vis[i] * 2
        vis[i] += 1
        arr[a2] += 1
        arr[a3] += 1
        arr[a4] += 1
        # print("ans = ",answer)
        # print("i = ",a2,a3,a4)
    return answer