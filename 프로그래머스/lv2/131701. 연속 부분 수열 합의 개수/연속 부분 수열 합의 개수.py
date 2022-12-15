def solution(elements):
    arr = []
    answer = 0
    n = len(elements)
    elements += elements
    for i in range(1,n):
        for j in range(0,len(elements)):
            arr.append(sum(elements[j:j+i]))
    arr = set(arr)
    return len(arr)+1