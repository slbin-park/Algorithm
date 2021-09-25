n, k = map(int, input().split())
idx = 0
res = []  #len(res) 는 a의 개수 , a의 인덱스가 들어갈거임
cnt = 0
bcnt = n - 1  # b의 개수
for i in range(n):
    if cnt == k:
        break
    cnt -= len(res)  #a가 한개 들어가므로 쌍의 개수가 1개씩 사라짐
    bcnt -= 1  #a가 들어가므로 b의 개수가 줄어듬
    for j in range(n, idx, -1):
        if cnt + n - j == k:
            idx = j
            res.append(j)
            cnt += n - j
            break
        if idx == j - 1 and cnt + n - j <= k:
            idx = j
            res.append(idx)
            cnt += n - j
        elif cnt + n - j < k:
            continue
        elif cnt + n - j > k:
            idx = j + 1
            cnt += n - j - 1
            res.append(j + 1)
            break
if cnt != k:
    print(-1)
else:
    ans = ''
    for i in range(1, n + 1):
        if i in res:
            ans += 'A'
        else:
            ans += 'B'
    print(ans)
