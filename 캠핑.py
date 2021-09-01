i = 0
while 1:
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] == arr[2] == 0:
        break
    cnt = 0
    while 1:
        if arr[1] < arr[2]:
            arr[2] = arr[2]-arr[1]
            cnt += arr[0]
        else:
            cnt += min(arr[2], arr[0])
            break
    i += 1
    print('Case', i, end='')
    print(':', cnt)
