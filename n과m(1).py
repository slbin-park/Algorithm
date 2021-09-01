
n,m = map(int,input().split())
visited = [0 for i in range(n+1)]
arr = [0]*(n+2)
arr[0] = 0
def back(depth):
    if depth==m : 
        for j in range(1,n+1):
            if visited[j] == 0:
                for h in range(1,m):
                    print(arr[h],end=' ')
                print(j)
    else :
        for i in range(1,n+1):
            if(visited[i] ==0):
                visited[i] = 1 
                arr[depth] = i
                back(depth+1)
                visited[i] = 0
back(1)