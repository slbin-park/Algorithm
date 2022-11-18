def solution(number, limit, power):
    answer = 0
    arr = [0 for i in range(number+1)]
    for i in range(1,number+1):
        cnt = 1
        while i*cnt<=number:
            arr[i*cnt]+=1
            cnt+=1
    for i in range(1,number+1):
        if arr[i] > limit:
            answer+=power
        else:
            answer+=arr[i]
    return answer