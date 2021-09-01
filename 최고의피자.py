n = int(input())
a, b = map(int, input().split())
c = int(input())
arr = [0]*(n)
for i in range(n):
    arr[i] = int(input())
arr.sort(reverse=True)
cal = c
cnt = 1
res = c/a
for i in range(n):
    if (cal+arr[i])/(a+(b*cnt)) > res:
        res = (cal+arr[i])/(a+(b*cnt))
        cal += arr[i]
        cnt += 1

    else:
        break
print(int(res))
