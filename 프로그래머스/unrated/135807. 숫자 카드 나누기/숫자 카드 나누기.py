def solution(arrayA, arrayB):
    # 모든게 나눠지는지
    def check1(arr,x):
        for y in arr:
            if y%x !=0:
                return False
        return True
    # 모든게 안나눠지는지
    def check2(arr,x):
        for y in arr:
            if y%x ==0:
                return False
        return True
    answer = 0
    mina = min(arrayA)
    minb = min(arrayB)
    arra = []
    arrb = []
    for i in range(2,mina//2+1):
        if mina%i == 0:
            arra.append(i)
    arra.append(mina)
    arra.reverse()
    for i in range(2,minb//2+1):
        if minb %i == 0:
            arrb.append(i)
    arrb.append(minb)
    arrb.reverse()
    for i in arra:
        if check1(arrayA,i):
            if check2(arrayB,i):
                answer = i
                break;
    for i in arrb:
        if answer >= i:
            break
        if check1(arrayB,i):
            if check2(arrayA,i):
                answer = max(answer,i)
                break
    return answer