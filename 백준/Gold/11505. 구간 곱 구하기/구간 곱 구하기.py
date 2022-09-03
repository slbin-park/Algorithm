from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
from xml.dom.minicompat import NodeList
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))

def init(node,start,end):
    if start==end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end) // 2
    left = init(node*2,start,mid)
    right = init(node*2+1,mid+1,end)
    tree[node] = (left*right)%1000000007
    return tree[node]

def submul(node,start,end,left,right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return submul(node*2,start,mid,left,right) * submul(node*2+1,mid+1,end,left,right)%1000000007


def update(node,start,end,prev_value,value,index):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = value
        return
    mid = (start+end) // 2
    update(node*2,start,mid,prev_value,value,index)
    update(node*2+1,mid+1,end,prev_value,value,index)
    tree[node] = tree[node*2] * tree[node*2+1] % 1000000007

n , m , k = map(int,input().split())
arr = []
tree = [0] * (n * 4)
for i in range(n):
    arr.append(int(input()))
init(1,0,n-1)
for i in range(m+k):
    a,b,c, = map(int,input().split())
    if a==1:
        update(1,0,n-1,arr[b-1],c,b-1)
    else:
        print(submul(1,0,n-1,b-1,c-1))