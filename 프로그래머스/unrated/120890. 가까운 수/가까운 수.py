def solution(array, n):
    answer = 0
    for i in range(len(array)):
        if abs(n-answer) > abs(array[i]-n):
            answer = array[i]
        elif abs(n-answer) == abs(array[i]-n):
            answer = answer if answer < array[i] else array[i]
    return answer