n = int(input())
arr = list(map(int, input().split()))
m = int(input())
cnt = 0
for i in arr:
    if i == m:
        cnt += 1
print(cnt)
