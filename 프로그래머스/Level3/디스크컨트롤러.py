import heapq


def solution(jobs):
    answer = 0
    heap = []
    now = 0
    j = 0
    start = -1
    while j < len(jobs):
        # 힙에는 시작시간은 넘었지만 시작하지 않은것을 넣어줌
        # 그러면 처음들어오는것 의 end타임을 index로 넣고
        # 그것의 시작시간보다 크고 현재시간보다 같거나 작은것을
        # 힙에 넣어줌
        for i in range(len(jobs)):
            if start < jobs[i][0] <= now:
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
        if len(heap) >= 1:
            end_time, start_time = heapq.heappop(heap)
            start = now
            now += end_time
            answer += now - start_time
            j += 1
        else:
            now += 1
    print(answer)
    return answer // len(jobs)


solution([[0, 3], [1, 9], [2, 6]])