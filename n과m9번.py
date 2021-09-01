n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [0 for i in range(n+1)]
li = []
arr2 = {}
def back(depth):
    if depth==m : 
        a = ''
        for i in li :
            a+=str(i) + " "
        if a not in arr2:
            arr2[a] = 1
            print(a)
        return ;
    else :
        for i in range(n):
                if(visited[i] ==0):
                    visited[i] = 1
                    li.append(arr[i])
                    visited[i] = 0
                    li.pop()
back(0)
