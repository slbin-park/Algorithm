n, m = map(int, input().split())
arr = [[] for i in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    arr[i] = [a, b]
arr.sort(key=lambda x: x[0])
ans1 = (n // 6) * arr[0][0]
ans0 = arr[0][0]
arr.sort(key=lambda x: x[1])
ans2 = (n % 6) * arr[0][1]
res = min(ans1 + ans0, ans1 + ans2, arr[0][1] * n)
print(res)
