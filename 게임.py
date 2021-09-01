n, m = map(int, input().split())
res = m*100//n
cnt = 0
left, right = 1, 1000000000
y = -1
while left <= right:
    mid = (left+right)//2
    if (m+mid)*100//(n+mid) <= res:
        left = mid+1
    else:
        y = mid
        right = mid-1
print(y)
