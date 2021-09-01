n = int(input())
d =[0 for i in range(n+1)]#배열 초기화
d[2] = 2
d[1] = 1
for i in range(3,n+1):
    d[i] = (d[i-1]+d[i-2])%15746
print(d[n])