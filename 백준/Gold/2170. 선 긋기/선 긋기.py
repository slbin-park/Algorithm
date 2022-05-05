import sys

input = sys.stdin.readline
n = int(input())
arr = []
answer = 0
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()
start = arr[0][0]
end = arr[0][1]
for i in range(1, n):
    cur_s = arr[i][0]
    cur_e = arr[i][1]
    if end > cur_s:
        end = max(end, cur_e)
    else:
        answer += end - start
        start = cur_s
        end = cur_e
answer += end - start
print(answer)