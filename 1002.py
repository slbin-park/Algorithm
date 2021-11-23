import math

n = int(input())
for _ in range(n):  # 1부터 5까지
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if (distance == 0 and r1 == r2):
        print(-1)
    elif (distance == abs(r1 - r2) or distance == r1 + r2):
        print(1)
    elif (abs(r1 - r2) < distance < r1 + r2):
        print(2)
    else:
        print(0)
# 송승준병신