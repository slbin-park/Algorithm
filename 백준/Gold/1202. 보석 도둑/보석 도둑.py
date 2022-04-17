import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

gem = []
weights = []

for _ in range(N):
  M,V = map(int, input().split())
  heapq.heappush(gem, [M,V])

for _ in range(K):
  heapq.heappush(weights, int(input()))

sum = 0

capable_gem = []

for _ in range(K):
  capacity = heapq.heappop(weights)
  
  while gem and capacity >= gem[0][0]:
    [weight, price] = heapq.heappop(gem)
    heapq.heappush(capable_gem, -price)
  
  if capable_gem:
    sum -= heapq.heappop(capable_gem)
  elif not gem:
    break

print(sum)