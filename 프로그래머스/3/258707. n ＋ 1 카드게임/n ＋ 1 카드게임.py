def solution(coin, cards):
    answer = 0
    cnt = 1
    nSum = len(cards) + 1
    
    # 0 = notSelect
    # 1 = use
    # 2 = firstSelectedCard
    visited = [0 for i in range(len(cards))]
    for i in range(len(cards)//3):
        visited[i] = 2
        
    for i in range(len(cards)//3):
        if visited[i] == 1:
            continue
        for j in range(i+1,len(cards)//3):
            if cards[i] + cards[j] == nSum and visited[j] == 2:
                cnt += 1
                visited[i] = 1
                visited[j] = 1
                break
    realCnt = cnt
    realCoin = coin
    for _ in range(coin + coin//2 + 1):
        selected = 0
        if realCoin == 0 :
            break
        # print("i, cnt ",i , cnt)
        for j in range(len(cards)//3):
            # 이미 사용한거면 넘어감
            if visited[j] == 1:
                continue
            # 처음 뽑고 사용안한것들 중에
            for k in range(len(cards)//3, len(cards)//3 + ((cnt)*2)):
                if k >= len(cards):
                    break
                if cards[j] + cards[k] == nSum and visited[k] == 0:
                    # print("selected ",j,k)
                    selected = 1
                    cnt += 1
                    visited[j] = 1
                    visited[k] = 1
                    realCoin -= 1
                    break
            if selected == 1:
                break
        if selected == 0 and realCoin >= 2:
            for j in range(len(cards)//3, len(cards)//3 + ((cnt)*2)):
                if j >= len(cards):
                    break
                if visited[j] == 0:
                    for k in range(j+1, len(cards)//3 + ((cnt)*2)):
                        if cards[j] + cards[k] == nSum and visited[j] == 0:
                            # print("success?",j,k)
                            visited[j] = 1
                            visited[k] = 1
                            realCoin -= 2
                            cnt += 1
                            selected = 1
                            break
                if selected == 1:
                    break
    # print(cnt)
    # print(realCnt)
    return min(cnt , (len(cards) - len(cards)//3)//2+1)