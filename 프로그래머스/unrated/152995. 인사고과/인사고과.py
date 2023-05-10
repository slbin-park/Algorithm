def solution(scores):
    answer = -1
    arr = []
    scArr = []
    for i in range(len(scores)):
        arr.append([scores[i][0],scores[i][1],i])
    arr.sort(key=lambda x:[-x[0],x[1]])
    # print(arr)
    maxV = -1
    for i in range(len(arr)):
        maxV = max(maxV,arr[i][1])
        if(maxV > arr[i][1]):
            if arr[i][2]==0:
                return -1
            continue
        else:
            scArr.append([arr[i][0],arr[i][1],arr[i][2]])
    scArr.sort(key=lambda x :[-(x[0]+x[1]),x[2]])
    # print(scArr)
    for i in range(len(scArr)):
        if scArr[i][2] == 0:
            return i+1
    return answer