def solution(money):
    answer = 0
    n = len(money)
    arr = [0 for i in range(n)]
    arr[0] = money[0]
    arr[1] = max(money[1],arr[0])
    for i in range(2,n):
        arr[i] = max(arr[i-1], arr[i-2] + money[i])
    answer = arr[-2]
    
    arr2 = [0 for i in range(n)]
    arr2[0] = 0
    arr2[1] = max(money[1],arr2[0])
    for i in range(2,n):
        arr2[i] = max(arr2[i-1], arr2[i-2] + money[i])
    
    return max(answer,arr2[-1])