def solution(bridge_length, weight, truck_weights):
    answer = 0
    arr = [0] * bridge_length
    sum_arr = 0
    while len(arr):
        answer += 1
        a = arr.pop(0)
        if a > 0:
            sum_arr -= a
        if truck_weights:
            if sum_arr + truck_weights[0] <= weight:
                b = truck_weights.pop(0)
                arr.append(b)
                sum_arr += b
            else:
                arr.append(0)
    return answer