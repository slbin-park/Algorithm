a,b = map(int,input().split())
arr = list(map(int,input().split()))
bj = 0
for i in range(a):
    for j in range(a):
        if(j>i):
            for t in range(a):
                if(j<t):
                    if(arr[i]+arr[j]+arr[t]<=b):
                        if(bj<arr[i]+arr[j]+arr[t]):
                            bj = arr[i]+arr[j]+arr[t]
print(bj)
