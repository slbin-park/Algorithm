res = 0
number = 0
for i in range(5):
    arr = list(map(int, input().split()))
    if res < sum(arr):
        res = sum(arr)
        number = i+1
print(number, res)
