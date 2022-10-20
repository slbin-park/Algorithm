import sys
import heapq
from copy import deepcopy
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
m = int(input())
arr1= []
if m !=0:
    arr1 = list(map(int,input().split()))
arr = []
for i in range(10):
    if i not in arr1:
        arr.append(i)
diff = abs(100-n)
number = 0
res = 0
str1 = ['0']
def dfs():
    if len(str1)>1:
        cal(int(''.join(str1)))
    if len(str1) <= len(str(n))+1:
        for a in arr:
            str1.append(str(a))
            dfs()
            str1.pop()

def cal(diff_num):
    global number,diff
    if abs(diff_num-n)+len(str1)-1 < diff:
        number = diff_num
        diff = abs(diff_num-n)+len(str1)-1
dfs()
print(diff)