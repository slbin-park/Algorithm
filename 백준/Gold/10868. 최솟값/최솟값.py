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
        tree[node] = min(init(node*2, start, (start+end)//2) , init(node*2+1, (start+end)//2+1, end))
        return tree[node]
def getmin(node,start,end,left,right):
    # start,end node가 담당해야하는 구간
    # left , right 합을 구해야하는 구간
    
    # 겹치지 않으면 종료
    if left>end or right < start:
        return 1e9 +1

    if left<=start and end <= right:
        return tree[node]
    return min(getmin(node*2, start, (start+end)//2, left, right) , getmin(node*2+1,(start+end)//2+1,end,left,right))

n , m = map(int,input().split())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())
tree = [0] * 30000000
init(1,0,n-1)
for i in range(m):
    a ,b = map(int,input().split())
    print(getmin(1, 0, n-1 ,a-1, b-1))