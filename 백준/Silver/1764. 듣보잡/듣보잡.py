import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dic = {}
answer = []
for i in range(n):
    a = input().strip()
    dic[a] = 1
for i in range(m):
    a = input().strip()
    try:
        dic[a] += 1
        answer.append(a)
    except:
        continue
answer.sort()
print(len(answer))
for i in answer:
    print(i)