n,m = map(int,input().split())
visited = [0 for i in range(n+1)]
li = []

def back(depth):
    if depth==m : 
        print(*li)
    else :
        for i in range(1,n+1):
            if visited[i] == 0:
                visited[i] = 1 
                li.append(i)
                back(depth+1)
                li.pop()
                visited[i] = 0
back(0)