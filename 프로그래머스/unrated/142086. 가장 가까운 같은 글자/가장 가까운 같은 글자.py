def solution(s):
    dic= {}
    answer = []
    for i in range(len(s)):
        a = s[i]
        if a in dic:
            answer.append(i-dic[a])
            dic[a] = i
        else:
            answer.append(-1)
            dic[a] = i
    return answer