def solution(skill, skill_trees):
    skil = len(skill)
    answer = 0
    lst = ['' for i in range(skil)]
    for i in range(skil):
        lst[i] = skill[i]

    for item in skill_trees:
        flag = 1
        prev = -1
        prev_skill = -1
        for i in range(skil):
            if lst[i] in item:
                if prev > item.index(lst[i]) or prev_skill != i - 1:
                    flag = 0
                    break
                else:
                    prev = item.index(lst[i])
                    prev_skill += 1
        if flag == 1:
            answer += 1

    return answer