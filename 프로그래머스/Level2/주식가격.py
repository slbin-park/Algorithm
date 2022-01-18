import heapq


def solution(prices):
    answer = [0 for i in range(len(prices))]
    heap = []
    heapq.heappush(heap, (-prices[0], 0))
    for i in range(1, len(prices)):
        while len(heap) > 0 and heap[0][0] < -prices[i]:
            price, idx = heapq.heappop(heap)
            answer[idx] = i - idx
        heapq.heappush(heap, (-prices[i], i))
    while heap:
        a, idx = heapq.heappop(heap)
        answer[idx] = len(prices) - idx - 1

    return answer