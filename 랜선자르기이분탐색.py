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

    # if(abs(right-left)==1 or right==left):
    #     c=0
    #     for j in range(a):
    #         c+=int(arr[j]/right)
    #     if(c>=b):
    #         if(d<right):
    #             d=right
    #     c=0
    #     for j in range(a):
    #         c+=int(arr[j]/left)
    #     if(c>=b):
    #         if(d<left):
    #             d=left
    #     arrc=False
    #     break;


        




# graph = [input() for _ in range(a)] 문자열 받기
