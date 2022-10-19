import sys
import heapq
from copy import deepcopy
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
arr = []
dic = {}
for i in range(n):
    arr.append(input().rstrip())

last_num = 9
arr2 = deepcopy(arr)
while arr2:
    arr2.sort(key=lambda x: len(x))
    a = arr2.pop()
    try:
        dic[a[0]] += 10**len(a)
    except:
        dic[a[0]] = 10**len(a)
    if a[1:] != '':
        arr2.append(a[1:])
dic = sorted(dic.items())
dic.sort(key=lambda x:-x[1])
dic2 = {}
for str2,b in dic:
    dic2[str2] = last_num
    last_num-=1
res = 0
for i in range(n):
    cur_str = ''
    for j in range(len(arr[i])):
        cur_str+=str(dic2[arr[i][j]])
    res += int(cur_str)
print(res)