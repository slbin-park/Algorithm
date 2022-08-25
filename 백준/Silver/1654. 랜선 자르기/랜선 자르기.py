a,b = map(int,input().split())
arr = [int(input()) for _ in range(a)]
d = 0
arrc = True
left=1
right=max(arr)
while  left <= right :
    mid = (left+right)//2
    c=0
    for j in range(a):
        c+=arr[j]//mid
    if(c>=b):
        if(d<mid):
            d=mid
        left=mid+1
    elif(c<b):
        right=mid-1
print(d)