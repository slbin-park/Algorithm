def bi_search(start, end):
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in range(1, n + 1):
            temp += min(n, mid // i)
        if temp >= m:
            end = mid - 1
        else:
            start = mid + 1
    return mid


n = int(input())
m = int(input())
arr = []
res = bi_search(1, n * n)
print(res)
