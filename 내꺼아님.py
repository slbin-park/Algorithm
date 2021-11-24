def DigitSum(x):
    result = 0
    quo = x
    while (True):
        print(result)
        if quo == 0:
            break
        result += quo % 10
        quo = quo // 10
    return result


Num = int(input("정수를 입력하시오."))
print("%d 의 각자리 수의 합은 %d입니다." % (Num, DigitSum(Num)))
