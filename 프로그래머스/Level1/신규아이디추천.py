def solution(new_id):
    answer = ''
    # 1. 모두 소문자로 변경
    new_id = new_id.lower()
    print("1번 = ", new_id)

    # 2. 소문자,숫자,-,_,.를 제외한 모든 문자를 제거
    cur = ''
    for i in range(len(new_id)):
        a = new_id[i]
        if a.isdigit() or a.isalpha() or a == '-' or a == '_' or a == '.':
            cur += a
    new_id = cur
    print("2번 = ", new_id)

    # 3. 마침표 두번연속이면 . 하나로 변경
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    print("3번 =  " + new_id)
    # 4. .이 첫번째거나 맨 뒤에 있으면 제거
    if len(new_id) >= 1:
        if new_id[0] == '.':
            new_id = new_id[1:len(new_id)]
        if len(new_id) >= 1:
            if new_id[-1] == '.':
                new_id = new_id[:len(new_id) - 1]
    print("4번 = ", new_id)
    # 5. 빈 문자열이면 'a'를 대입
    if new_id == '':
        new_id = 'a'

    # 6. 길이가 16개 이상이면 15개 빼고 제거 그리고 마침표가 마지막에 있으면 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            while new_id[-1] == '.':
                new_id = new_id[:len(new_id) - 1]
    print("6번 = ", new_id)

    #7. new_id 가 2자 이하라면 new_id의 문자를 길이가 3될때까지 반복
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id