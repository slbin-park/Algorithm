import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def sdoku(idx):
    if idx == len(ept):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end=' ')
            print('')
        exit(0)
    x = ept[idx][0]
    y = ept[idx][1]
    check_arr = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if arr[x][i] !=0:
            if arr[x][i] in check_arr:
                check_arr.remove(arr[x][i])
        if arr[i][y] !=0:
            if arr[i][y] in check_arr:
                check_arr.remove(arr[i][y])
    x2 =x//3
    y2 =y//3
    # for i in arr:
    #     print(i)
    # print()
    
    for p in range(x2*3, (x2+1)*3):
        for q in range(y2*3, (y2+1)*3):
            if arr[p][q] in check_arr:
                check_arr.remove(arr[p][q])
            
    if len(check_arr) == 0:
        return -1
    for i in check_arr:
        arr[x][y] = i
        if sdoku(idx+1) == -1:
            arr[x][y] = 0
    return -1
    
arr= [[[]for i in range(9)]for i in range(9)]
ept = []
for i in range(9):
    arr[i] = list(map(int,input().split()))
    for j in range(9):
        if arr[i][j] == 0:
            ept.append([i,j])
sdoku(0)
