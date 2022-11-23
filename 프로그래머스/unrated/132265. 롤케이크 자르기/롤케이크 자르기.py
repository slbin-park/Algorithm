def solution(topping):
    answer = 0
    visited = [0 for i in range(10001)]
    n = len(topping)
    arr = [0 for i in range(n)]
    arr2 = [0 for i in range(n)]
    cur_cnt = 0
    if len(topping) == 1:
        return answer
    if len(topping) == 2:
        return 1
    for i in range(n):
        if visited[topping[i]] == 0:
            cur_cnt+=1
            visited[topping[i]] = 1
            arr[i] = cur_cnt
        else:
            arr[i] = cur_cnt
    visited = [0 for i in range(10001)]
    cur_cnt = 0
    for i in range(n-1,-1,-1):
        if visited[topping[i]] == 0:
            cur_cnt+=1
            visited[topping[i]] = 1
            arr2[i] = cur_cnt
        else:
            arr2[i] = cur_cnt
    for i in range(n-2):
        if arr[i] == arr2[i+1]:
            answer+=1
    return answer