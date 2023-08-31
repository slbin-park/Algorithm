import heapq
def solution(book_time):
    answer = 0
    book_time.sort()
    heap = []
    for i in range(len(book_time)):
        # print(heap)
        if len(heap) == 0:
            heapq.heappush(heap,book_time[i][1])
            answer+=1
        else:
            cur_time = heap[0]
            t,m = cur_time.split(":")
            cur_time2 = book_time[i][0]
            t2,m2 = cur_time2.split(":")
            t = int(t)
            m = int(m) + 10
            t2 = int(t2)
            m2 = int(m2)
            tmp = (t2*60+m2)-(t*60+m)
            # print("tmp",tmp)
            # print(cur_time,cur_time2)
            if tmp>=0:
                heapq.heappop(heap)
                heapq.heappush(heap,book_time[i][1])
            else:
                answer+=1
                heapq.heappush(heap,book_time[i][1])
    return answer