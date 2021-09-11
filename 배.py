import sys

input = sys.stdin.readline

n = int(input())
crain = list(map(int, input().split()))

m = int(input())
weight = list(map(int, input().split()))
weight.sort(reverse=True)
crain.sort(reverse=True)
time = 0
if max(weight) > max(crain):
    print(-1)
else:
    while weight:
        for i in range(n):
            for j in range(len(weight)):
                if crain[i] >= weight[j]:
                    del weight[j]
                    break
        time += 1
    print(time)
