n,m = map(int,input().split())
visited = [0 for i in range(n+1)]
li = []
prev = 0
# li[-1] - > 
def back(depth):
    global prev
    if depth==m : 
        print(*li)
    else :
        for i in range(1,n+1):
            if visited[i] == 0:
                if(i>=prev):
                    visited[i] = 1 
                    li.append(i)
                    prev = i
                    back(depth+1)
                    prev = 0
                    li.pop()
                    visited[i] = 0
back(0)