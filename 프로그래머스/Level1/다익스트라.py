import heapq
from turtle import distance  # 우선순위 큐 구현

graph = {
    'A': {
        'B': 8,
        'C': 1,
        'D': 2
    },
    'B': {},
    'C': {
        'B': 5,
        'D': 2
    },
    'D': {
        'E': 3,
        'F': 5
    },
    'E': {
        'F': 1
    },
    'F': {
        'A': 5
    }
}


def dijkstra(graph, start):
    distances = {node: float('inf')
                 for node in graph}  # start로 부터 거리 값을 저장하기 위함
    distances[start] = 0  # 시작값은 0 이여야함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작노드부터 탐색 시작 하기 위함
    while queue:  # 큐가 존재하면
        cur_dis, cur_desti = heapq.heappop(queue)  # 탐색할 노드 , 거리를 불러옴
        if distances[cur_desti] < cur_dis:  # 기존에 있는 거리보다 길다면 넘어감
            continue
        for new_de, new_di in graph[cur_desti].items():
            distance = cur_dis + new_di  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_de]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_de] = distance
                heapq.heappush(queue,
                               [distance, new_de])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return distances


INF = 1e9
n = 10


def dijkstra(start, end):
    heap = []  # 우선순위 큐를 생성함
    heapq.heappush(heap, (0, start))  # [가중치,시작번호]
    dis = [INF] * (n + 1)  # 간선 개수
    dis[start] = 0  # 시작정점은 거리가 무조건 0

    while heap:
        cos, index = heapq.heappop(heap)  # [간선의 가중치 , 노드 번호]
        if dis[index] < cos:  # 거리가 멀다면 넘어감
            continue
        for e, c in bus[index]:  # [ , ]
            if dis[e] > cos + c:
                dis[e] = cos + c
                heapq.heappush(heap, (cos + c, e))
    return dis[end]
