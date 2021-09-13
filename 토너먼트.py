n, m, k = map(int, input().split())
if m > k:
    temp = m
    m = k
    k = temp
arr = [i for i in range(1, n + 1)]
cnt = 0
check = 1
while check:
    for i in range((len(arr) - 1) // 2):
        if i + 1 > len(arr) - 1:
            break
        else:
            if arr[i] == m:
                print(arr[i], arr[i + 1])
                if arr[i + 1] == k:
                    check = 0
                    break
            elif arr[i] == m or arr[i] == k:
                del arr[i + 1]
            else:
                del arr[i]
    print(arr)
    cnt += 1
print(cnt)
