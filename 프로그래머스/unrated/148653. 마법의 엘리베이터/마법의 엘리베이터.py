from collections import deque
def solution(storey):
    answer = 1e9
    dq = deque()
    dq.append([storey,0])
    while dq:
        index,cost = dq.popleft()
        if index == 0:
            answer = min(answer,cost)
        elif index<10:
            a = min(index , 10-index+1)
            answer = min(answer,cost + a)
        else:
            if index>=10:
                dq.append([(index+10)//10,cost+10 - (index % 10)])
            dq.append([index//10,cost + (index % 10)])
    return answer