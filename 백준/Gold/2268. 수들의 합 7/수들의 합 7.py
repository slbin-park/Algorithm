import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline



def init(node,start,end):
    if start==end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = (start+end)//2
        tree[node] = init(node*2,start,mid) + init(node*2+1,mid+1,end)
        return tree[node]

def update(node,start,end,index,diff):
    if index < start or end < index:
        return
    tree[node] += diff
    
    mid = (start+end)//2
    if start!=end:
        update(node*2,start,mid,index,diff)
        update(node*2+1,mid+1,end,index,diff)

def query(node,start,end,left,right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return query(node*2,start,mid,left,right) + query(node*2+1,mid+1,end,left,right)

n , m = map(int,input().split())
arr = [0 for i in range(n)]
tree = [0] * (n*4+1)
for i in range(m):
    fun , left , right = map(int,input().split())
    if fun == 0:
        if left > right:
            tmp = right
            right = left
            left = tmp
        print(query(1,0,n-1,left-1,right-1))
    else:
        left -=1
        diff = right - arr[left]
        arr[left] = right
        update(1,0,n-1,left,diff)