def solution(queue1, queue2):
    answer = 0
    left = 0 
    right = len(queue1)-1
    result = (sum(queue1)+sum(queue2))//2
    cur_value = sum(queue1)
    if result == cur_value:
        return 0
    queue1 += queue2
    while right < len(queue1)-1:
        if cur_value < result:
            right+=1
            cur_value+= queue1[right]
        elif cur_value > result:
            cur_value-=queue1[left]
            left+=1
        answer+=1
        if cur_value == result:
            return answer
    return -1