import sys
sys.setrecursionlimit(10**8)
dic = {}
def solution(k, room_number):
    global dic
    answer = []
    def find(x):
        global dic
        if dic[x] != x:
            dic[x] = find(dic[x])
            return dic[x]
        return dic[x]
    for room in room_number:
        if room in dic:
            a = find(room)
            b = a+1
            if a+1 in dic:
                b = find(a+1)
            dic[a] = b
            dic[b] = b
            answer.append(a)
        else:
            if room+1 in dic:
                b = find(room+1)
                dic[room] = b
                dic[b] = b
            else:
                dic[room] = room+1
                dic[room+1] = room+1
            answer.append(room)
    return answer