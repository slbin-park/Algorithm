n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [0 for i in range(n+1)]
li = []
prev=0
def back(depth):
    global prev
    if depth==m : 
        print(*li)
    else :
        for i in range(0,n):
            if(arr[i]>=prev):
                prev=arr[i]
                li.append(arr[i])
                back(depth+1)
                prev=0
                li.pop()
back(0)