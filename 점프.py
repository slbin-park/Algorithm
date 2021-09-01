n = int(input())
arr = [[int(x) for x in input().split()] for j in range(n)]
count=0
arr2 = [[0 for i in range(n)] for j in range(n)]
arr2[0][0] =1 
for i in range(n):
    for j in range(n):
        if(i==n-1 and j==n-1):
            break;
        else:
            if(arr2[i][j]!=0):
                if(j+arr[i][j] < n):
                    arr2[i][j+arr[i][j]] += arr2[i][j]
                if(i+arr[i][j] < n):
                    arr2[i+arr[i][j]][j] += arr2[i][j]
print(arr2[n-1][n-1])
