n = int(input())
arr = [0 for i in range(n)]
for i in range(1, n + 1):
    arr[i - 1] = i


def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


res = permute(arr)
res.sort()
for i in range(len(res)):
    for j in range(n):
        print(res[i][j], end=' ')
    print()
