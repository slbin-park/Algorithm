def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    j = 0
    for i in range(len(participant)):
        if i>=len(completion):
            return participant[i]
        if participant[i] == completion[i]:
            continue;
        else:
            return participant[i]
    return participant[-1]