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
arr = list(map(int,input().split()))
tree = [0] * (n*4+1)
init(1,0,n-1)
for i in range(m):
    left , right , index ,value = map(int,input().split())
    if left > right:
        tmp = right
        right = left
        left = tmp
    
    print(query(1,0,n-1,left-1,right-1))
    
    index-=1
    diff = value - arr[index]
    arr[index] = value 
    
    update(1,0,n-1,index,diff)