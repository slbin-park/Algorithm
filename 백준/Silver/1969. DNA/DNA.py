import sys
import heapq
input = sys.stdin.readline
arr = []
n,m = map(int,input().split())
res = [''for i in range(m)]
answer = 0
for i in range(n):
    a = input().strip()
    arr.append(a)
for i in range(m):
    dic = {}
    for j in range(n):
        try:
            dic[arr[j][i]]+=1
        except:
            dic[arr[j][i]]=1
    cur = sorted(dic)
    max_num = 0
    for key in cur:
        if dic[key] >max_num:
            max_num = dic[key]
            res[i] = key
    answer+=n-max_num
print(''.join(res))
print(answer)