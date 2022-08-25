n = int(input())
ti = [0 for i in range(1,23)]
pi = [0 for i in range(1,23)]
result = [0 for i in range(1,23)]
maxn = 0
for i in range(1,n+1):
    t,p = map(int,input().split())
    ti[i] = t
    if(t+i>n+1):
        pi[i] = 0
    else:
        pi[i] = p

for i in range(1,n+1):
    if i+ti[i] <= (n+1):
        result[i+ti[i]] = max(result[i+ti[i]],result[i] + pi[i])
    result[i+1] =max(result[i+1],result[i])
print(result[n+1])

