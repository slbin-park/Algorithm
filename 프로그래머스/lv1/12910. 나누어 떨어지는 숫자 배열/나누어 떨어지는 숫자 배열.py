def solution(arr, divisor):
    answer = []
    arr.sort()
    for num in arr:
        if num%divisor ==0:
            answer.append(num)
    if len(answer) == 0:
        return [-1]
    return answer