import sys
sys.setrecursionlimit(10**9)
def solution(enroll, referral, seller, amount):
    answer = []
    dic = {}
    name_dic = {}
    result = [0 for i in range(len(enroll))]
    for i in range(len(enroll)):
        name_dic[i] = enroll[i]
        name_dic[enroll[i]] = i
    for i in range(len(referral)):
        # 추천인
        name = referral[i]
        # 추천으로 들어온 사람
        c_name = enroll[i]
        if name != "-":
            dic[c_name] = name
        else:
            dic[c_name] = ""
    for i in range(len(seller)):
        idx = name_dic[seller[i]]
        c_amount = amount[i]
        result[idx] += c_amount*100 - c_amount*100//10
        profit = c_amount*100//10
        name = dic[seller[i]]
        while name != "" and profit != 0:
            idx = name_dic[name]
            result[idx] += profit - profit//10
            profit = profit//10
            name = dic[name]
    return result