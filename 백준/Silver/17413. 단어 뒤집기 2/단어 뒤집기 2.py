import sys
import heapq
input = sys.stdin.readline
a = input().rstrip()
stack = []
flag = 0
res = ''
for i in range(len(a)):
    if flag == 0:
        if a[i]=='<':
            while stack:
                res+=stack.pop()
            flag=1
            res+=a[i]
        elif a[i]== ' ':
            while stack:
                res+=stack.pop()
            res+=' '
        elif a[i] != ' ':
            stack.append(a[i])
    else:
        res+=a[i]
        if a[i]=='>':
            flag=0
while stack:
    res+=stack.pop()
print(res)