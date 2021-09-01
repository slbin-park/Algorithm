import sys
input = sys.stdin.readline

n = int(input())
result = 0
i = 1
while True:
    i += 1
    result += i
    if result >= n:
        break

print(i-1)
