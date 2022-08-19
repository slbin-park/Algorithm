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
        left = init(node*2,start,mid)
        right = init(node*2+1,mid+1,end)
        tree[node] = min(left,right)
        return tree[node]

def update(node,start,end,index):
    if index < start or end < index:
        return tree[node]
    if start==end:
        tree[node] = arr[index]
        return tree[node]
    mid = (start+end)//2
    left = update(node*2,start,mid,index)
    right = update(node*2+1,mid+1,end,index)
    tree[node] = min(left,right)
    return tree[node]
    
def query(node,start,end,left,right):
    if left > end or right < start:
        return 1e9+1
    if left <= start and end <= right : 
        return tree[node]
    mid = (start+end)//2
    v_left = query(node*2,start,mid,left,right)
    v_right = query(node*2+1,mid+1,end,left,right)
    return min(v_left,v_right)
        
n  = int(input())
arr = list(map(int,input().split()))
tree = [0] * (n*4+1)
init(1,0,n-1)
m = int(input())
for i in range(m):
    fun , idx , value = map(int,input().split())
    if fun == 2:
        print(query(1,0,n-1,idx-1,value-1))
    else:
        idx -= 1
        arr[idx] = value
        update(1,0,n-1,idx)