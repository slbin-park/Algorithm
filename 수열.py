n, m = map(int, input().split())
arr = list(map(int, input().split()))
sumres = sum(arr[0:m])
res = sumres
prev = sumres
for i in range(m, n):
    prev = prev-arr[i-m]+arr[i]
    if res < prev:
        res = prev
if n != m:
    print(res)
else:
    print(sumres)
