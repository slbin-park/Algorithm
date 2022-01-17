import sys
from collections import deque
dq = deque()
inp = input().stip()
res = ''
flag = 0
for i in range(len(inp)):
    if flag==0:
        if inp[i] =='(':
            flag==1
        elif inp[i] == '+':
            