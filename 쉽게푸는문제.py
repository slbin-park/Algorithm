import sys
input = sys.stdin.readline

a,b = map(int,input().split())
arr=[0]
count=1
for i in range(1,b):
    for j in range(count):
        arr.append(count)
    count+=1


print(sum(arr[a:b+1]))