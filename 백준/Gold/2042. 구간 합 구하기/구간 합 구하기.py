import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def init(node,start,end):
    # node = 현재 노드
    # start = 구간합 구힐 시작 노드
    # end = 구간합 구할 마지막 노드
    if start == end :
        tree[node] = arr[start]
        return tree[node]
    else :
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장.
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]
def subsum(node,start,end,left,right):
    # start,end node가 담당해야하는 구간
    # left , right 합을 구해야하는 구간
    
    # 겹치지 않으면 종료
    if left>end or right < start:
        return 0  

    if left<=start and end <= right:
        return tree[node]
    return subsum(node*2, start, (start+end)//2, left, right) + subsum(node*2+1,(start+end)//2+1,end,left,right)

def update(node, start, end, index, diff) :
     
    if index < start or index > end :
        return
 
    tree[node] += diff
    
    # 리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에 검사해야함.
    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

n , m , k = map(int,input().split())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())
tree = [0] * 3000000
init(1,0,n-1)
for _ in range(m+k) :
    a, b, c = map(int, input().rstrip().split())
 
    if a == 1 :
        b = b-1
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, n-1, b, diff)
    elif a == 2 :                
        print(subsum(1, 0, n-1 ,b-1, c-1))