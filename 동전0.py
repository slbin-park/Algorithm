import sys
input = sys.stdin.readline

n , m = map(int,input().split())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())
arr.reverse()

cnt = 0 
value = m
for i in range(n):
    if(arr[i]<=value):
        cnt += value//arr[i]
        value = value%arr[i]
    if(value==0):
        break;
print(cnt)
