from copy import deepcopy
def cal(discount,dic2,index):
    dic2 = deepcopy(dic2)
    for i in range(index,index+10):
        try:
            dic2[discount[i]]-=1
            if dic2[discount[i]] <0:
                return False
        except:
            return False
    return True
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(number)):
        dic[want[i]] = number[i]
    for i in range(len(discount)-9):
        if cal(discount,dic,i):
            answer+=1
    return answer