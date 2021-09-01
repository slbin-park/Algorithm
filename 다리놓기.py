t = int(input())
arr = [0 for i in range(40)]  # 배열 초기화
arr[0] = 1
arr[1] = 1
for i in range(t):
    n, m = map(int, input().split())
    if(n > m):
     print(0)
    elif(n == m):
      print(1)
    else:
        for i in range(m+1):
          if(i > 1):
              arr[i] = arr[i-1]*i
        print(arr[m]//(arr[m-n]*arr[n]))
