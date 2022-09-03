from copy import deepcopy
import sys
from collections import deque
from itertools import combinations
from xml.dom.minicompat import NodeList
sys.setrecursionlimit(10**5)
# list(combinations(items, 2))
input = sys.stdin.readline

def update(node,start,end,value,index):
    if index < start or end < index:
        return
    if start==end:
        tree[node] += value
        return
    mid = (start+end)//2
    update(node*2,start,mid,value,index)
    update(node*2+1,mid+1,end,value,index)
    tree[node] = tree[node*2] + tree[node*2+1]

def get_sum(node,start,end,left,right):
    if left > end or right < start:
        return 0
    if left<= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return get_sum(node*2,start,mid,left,right) + get_sum(node*2+1,mid+1,end,left,right)

n , q = map(int,input().split())
tree = [0] * (n*4)
for i in range(q):
    a,b,c = map(int,input().split())
    if a ==1 :
        update(1,0,n-1,c,b-1)
    else:
        print(get_sum(1,0,n-1,b-1,c-1))