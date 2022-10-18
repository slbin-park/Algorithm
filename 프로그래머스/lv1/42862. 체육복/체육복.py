def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    arr = []
    a = 0
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                arr.append(reserve[j])
                break;
    for i in lost:
        if i in arr:
            continue
        for j in reserve:
            if j not in arr:
                if j -1 <= i <= j+1:
                    arr.append(j)
                    break
    return n -len(lost) + len(arr)