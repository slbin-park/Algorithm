def bisearch(start, end):
    global ans
    while start <= end:
        mid = (start + end) // 2
        res = 0
        flag = 0
        for i in range(n):
            if par[i] // mid > 0:
                res += par[i] // mid
            if res >= m:
                flag = 1
                break
        if flag == 1:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1


n, m = map(int, input().split())
par = [0 for _ in range(n)]
ans = 0
parsum = 0
for i in range(n):
    par[i] = int(input())
    parsum += par[i]
bisearch(1, max(par))
parsum = parsum - (ans * m)
print(parsum)
