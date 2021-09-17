import itertools

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(itertools.combinations(arr, m))
res = []
for i in arr2:
    if sum(i) not in res:
        res.append(sum(i))
res.sort()
cnt = 0
for i in res:
    check = 0
    for j in range(2, i):
        if i % j == 0:
            check = 1
            break
    if check == 0:
        print(i, end=' ')
        cnt += 1
if cnt == 0:
    print(-1)
