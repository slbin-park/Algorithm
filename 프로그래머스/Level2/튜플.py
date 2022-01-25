def solution(s):
    answer = []
    s = s.replace('{', '')
    s = s.split('},')
    s[-1] = s[-1].replace('}', '')
    s.sort(key=lambda x: len(x))
    for i in range(len(s)):
        s[i] = s[i].split(',')
        for j in range(len(s[i])):
            if int(s[i][j]) not in answer:
                answer.append(int(s[i][j]))
    return answer