import heapq
def solution(n, roads, sources, destination):
    answer = []
    road = [[]for i in range(n+1)]
    dis = [1e9 for i in range(n+1)]
    for a,b in roads:
        road[a].append(b)
        road[b].append(a)
    heap = []
    heapq.heappush(heap,[0,destination])
    dis[destination] = 0
    while heap:
        cost,index = heapq.heappop(heap)
        for next in road[index]:
            if dis[next] > cost+1:
                dis[next] = cost+1
                heapq.heappush(heap,[cost+1,next])
    for i in sources:
        if dis[i] == 1e9:
            answer.append(-1)
        else:
            answer.append(dis[i])
    return answer