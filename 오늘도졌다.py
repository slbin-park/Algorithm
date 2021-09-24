arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
score1 = 0
score2 = 0
for i in range(9):
    score1 += arr1[i]
    if score1 > score2:
        print('Yes')
        exit(0)
    score2 += arr2[i]
print('No')
