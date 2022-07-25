import sys
from collections import deque
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N , M = map(int,input().split())
chicken = []
house = []
arr = [[]for i in range(N)]
result = 1e9
for i in range(N):
    arr[i] = list(map(int,input().split()))
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i,j])
for item in list(combinations(chicken, M)):
    cur = 0
    
    for i in range(len(house)):
        # 전에것들 중에 가장 작은값 보다 클 경우 중지
        if cur >=result:
            break
        cur_c = 1e9
        x = house[i][0]
        y = house[i][1]
        
        # 가장 가까운 치킨집 거리를 찾음
        for x1,y1 in item:
            cur_c = min(cur_c,abs(x-x1)+abs(y-y1))
        cur+=cur_c
    result = min(result,cur)
    # print(result)
print(result)