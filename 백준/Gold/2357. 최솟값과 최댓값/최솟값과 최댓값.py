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
        tree[node] = [arr[start],arr[start]]
        return [arr[start],arr[start]]
    else :
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장.
        left = init(node*2, start, (start+end)//2) 
        right = init(node*2+1, (start+end)//2+1, end)
        tree[node] = [min(left[0],right[0]),max(left[1],right[1])]
        return tree[node]

def get_min_max(node,start,end,left,right):
    # start,end node가 담당해야하는 구간
    # left , right 합을 구해야하는 구간
    # 겹치지 않으면 종료
    if left>end or right < start:
        return [1e9+1,0]

    if left<=start and end <= right:
        return tree[node]
    get_left = get_min_max(node*2, start, (start+end)//2, left, right)
    get_right = get_min_max(node*2+1,(start+end)//2+1,end,left,right)
    return [min(get_left[0],get_right[0]),max(get_left[1],get_right[1])]

n , m = map(int,input().split())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input())
tree = [0,0] * 3000000
init(1,0,n-1)
for i in range(m):
    a ,b = map(int,input().split())
    result = get_min_max(1, 0, n-1 ,a-1, b-1)
    print(result[0],result[1])