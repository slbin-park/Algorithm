def solution(numbers):
    answer = []
    dic = {}
    def getMinValue(number):
        v = bin(number)[2:]
        cnt = 0
        if len(v) >= 3:
            cV = "0" + v
            idx = [0,0]
            for i in range(len(cV)-1,-1,-1):
                if cV[i-1] == "1" and cV[i] == "0":
                    return number+1
                if cV[i-1] == "0" and cV[i] == "1":
                    idx[0] = i-1
                    idx[1] = i
                    break
            ans = ""
            for i in range(len(cV)):
                if i == idx[0]:
                    ans += "1"
                elif i == idx[1]:
                    ans += "0"
                else:
                    ans += cV[i]
            return int(ans,2)
        while True:
            cnt += 1
            curV = bin(number+cnt)[2:]
            cur_cnt = len(curV) - len(v)
            for i in range(len(v)):
                if cur_cnt > 2:
                    break
                if v[-i-1] != curV[-i-1]:
                    cur_cnt +=1
            if cur_cnt <= 2:
                dic[number] = number+cnt
                return number+cnt
        # print(v)
    for number in numbers:
        if number in dic:
            answer.append(dic[number])
        else:
            answer.append(getMinValue(number))
    return answer