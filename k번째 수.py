def bi_search(start, end):
    global res
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in range(1, n + 1):
            temp += min(n, mid // i)
        if temp >= m:
            res = mid
            end = mid - 1
        else:
            start = mid + 1


n = int(input())
m = int(input())
arr = []
res = 0
bi_search(1, m)
print(res)
