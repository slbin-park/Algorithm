def DFS(L):
    global cnt
    if L==m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n):
            if ch[i]==0:
                ch[i]=1
                ch[L]=arr[i]
                DFS(L+1)
                ch[i]=0

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
ch=[0]*(n+1)
cnt=0
DFS(0)
print(cnt)