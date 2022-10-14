import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    max_value = 0
    answer = 0
    for i in range(m-1,-1,-1):
        if arr[i] > max_value:
            max_value = arr[i]
        else:
            answer+=max_value-arr[i]
    print(answer)