def solution(cap, n, deli, pickups):
    answer = 0
    pick = 0
    drop = 0
    idx = n-1
    pLast = idx
    dLast = idx
    while idx >= 0:
        # if pick ==0 and deli[idx] > 0:
        #     answer += (idx+1)*2
        #     pick -= cap
        #     drop -= cap
        # if drop ==0 and pickups[idx] >0:
        #     answer += (idx+1)*2
        #     pick -= cap
        #     drop -= cap
        pick += deli[idx]
        drop += pickups[idx]
        # print("idx , answer = ",idx,answer)
        # print(pick,drop)
        if pick > 0:
            while pick>0:
                answer += (idx+1)*2
                pick -= cap
                drop -= cap
        if drop > 0:
            while drop>0:
                answer += (idx+1)*2
                pick -= cap
                drop -= cap
        idx-=1
    # print(pick,drop)
    return answer
