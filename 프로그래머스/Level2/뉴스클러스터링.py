def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    a = []
    b = []
    # 계산기 (교집합 / 합집합) * 65536
    # 문자열 나누기
    # 영어일 경우에만 넣어야함
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            a.append(str1[i:i + 2])

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            b.append(str2[i:i + 2])

    # 합집합
    # union = list(set(a) | set(b))

    # 교집합
    # intersection = list(set(a) & set(b))

    # 배열을 먼저 복사함
    a_temp = a.copy()
    a_result = a.copy()

    # 다중집합 합집합
    for i in b:
        if i not in a_temp:
            a_result.append(i)
        else:
            a_temp.remove(i)
    # 다중집합 교집함
    result = []
    for i in b:
        if i in a:
            a.remove(i)
            result.append(i)
    print(result)
    print(a_temp)
    print(a_result)
    if len(result) == 0 and len(a_result) == 0:
        return 65536
    else:
        return len(result) / len(a_result) * 65536


st1 = "handshake"
st2 = "shake hands"
print(solution(st1, st2))
