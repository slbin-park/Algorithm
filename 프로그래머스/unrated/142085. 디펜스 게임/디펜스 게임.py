import heapq
def solution(n, k, enemy):
    answer = len(enemy)
    heap = []
    cur_sum = 0
    for i in range(len(enemy)):
        a = enemy[i]
        cur_sum+= a
        heapq.heappush(heap,-a)
        if cur_sum>n:
            while k!=0 and cur_sum>n:
                b = heapq.heappop(heap)
                cur_sum+=b
                k-=1
        if cur_sum>n:
            answer=i
            break;
    return answer