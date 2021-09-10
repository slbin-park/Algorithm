number = 0
res = 0
for i in range(9):
    a = int(input())
    if res < a:
        res = a
        number = i
print(res)
print(number + 1)
