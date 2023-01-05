def get_index(index,arr):
    while index >= 0 and arr[index] == 0:
        index-=1
    return index
def solution(cap, n, deli, pickups):
    answer = 0
    l_index = get_index(n-1,deli)
    r_index = get_index(n-1,pickups)
    n-=1
    while l_index >= 0 or r_index >= 0:
        cur_l_index = l_index
        cur_r_index = r_index
        l_cnt = 0
        r_cnt = 0
        
        while l_index >= 0 and l_cnt <cap:
            l_cnt += deli[l_index]
            deli[l_index] = 0
            l_index-=1
        if l_cnt > cap:
            l_index += 1
            deli[l_index] = l_cnt - cap
        else:
            l_index = get_index(l_index,deli)
            
        while r_index >= 0 and r_cnt < cap:
            r_cnt += pickups[r_index]
            pickups[r_index] = 0
            r_index-=1
        if r_cnt > cap:
            r_index +=1
            pickups[r_index] = r_cnt - cap
        else:
            r_index = get_index(r_index,pickups)
            
        answer += (max(cur_l_index , cur_r_index)+1) *2
    return answer
