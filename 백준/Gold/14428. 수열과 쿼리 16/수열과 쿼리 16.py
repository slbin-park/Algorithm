import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline


def minIdx(x,y):
    if arr[x] == arr[y]:
        return min(x,y)
    elif arr[x] > arr[y]:
        return y
    else:
        return x

def init(node,start,end):
    if start==end:
        tree[node] = start
        return tree[node]
    else:
        mid = (start+end)//2
        tree[node] = minIdx(init(node*2,start,mid),init(node*2+1,mid+1,end));
        return tree[node]

def update(node,start,end,index):
    if index < start or end < index or start==end:
        return tree[node]
    mid = (start+end)//2
    tree[node] = minIdx(update(node*2,start,mid,index),update(node*2+1,mid+1,end,index))
    return tree[node]

def query(node,start,end,left,right):
    if start > right or end < left:
        return tree[0]
    elif left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return minIdx(query(node*2,start,mid,left,right),query(node*2+1,mid+1,end,left,right))

n = int(input())
arr = list(map(int,input().split()))
arr.append(1000000001)
tree = [0] * (n*4+1)
tree[0] = n

init(1,0,n-1)
m = int(input())

for i in range(m):
    inp = list(map(int,input().split()))
    if (inp[0] == 2):
        print(query(1,0,n-1,inp[1]-1,inp[2]-1)+1)
    else:
        # 업데이트 하기
        inp[1] -=1
        arr[inp[1]] = inp[2]
        update(1,0,n-1,inp[1])