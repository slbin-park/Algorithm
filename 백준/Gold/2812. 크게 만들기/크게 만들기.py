import sys
import heapq
from copy import deepcopy
input = sys.stdin.readline
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n ,m = map(int,input().split())
a = input().rstrip()
stack = []
for i in range(n):
    if len(stack) and m!=0:
        if int(stack[-1]) <= int(a[i]):
            while len(stack) and m!=0 and int(stack[-1]) < int(a[i]):
                stack.pop()
                m-=1
            stack.append(a[i])
        else:
            stack.append(a[i])
    else:
        stack.append(a[i])
while m !=0:
    stack.pop()
    m-=1
print(int(''.join(stack)))