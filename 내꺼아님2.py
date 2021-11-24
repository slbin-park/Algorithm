def Pyung2msq(value):
    return value * 3.3


def Msq2pyubg(value):
    return value / 3.3


def Cm2inch(value):
    return value * 0.394


def Inch2cm(value):
    return value / 0.394


def TempF2C(value):
    return 5.0 * (value - 32.0) / 9.0


def TempC2F(value):
    return value * 9.0 / 5.0 + 32.0


print("--------------------------------")
print("     1. 평 -> 제곱미터")
print("     2. 제곱미터 -> 평")
print("     3. 센티미터 -> 인치")
print("     4. 인치 -> 센티미터")
print("     5. 화씨온도 -> 섭씨온도")
print("     6. 섭씨온도 -> 화씨온도")
print("     7. 종료 0")
print("--------------------------------")

while (True):
    menu, value = map(float, input("원하는 메뉴와 값을 입력하시오. (예) 1 34  :").split())
    if menu == 1:
        print("%d평 ---> %.2f 제곱미터" % (value, Pyung2msq(value)))
        continue
    if menu == 2:
        print("%.2f 제곱미터 ---> %d평" % (value, Msq2pyubg(value)))
        continue
    if menu == 3:
        print("%d센티미터 ---> %.2f 인치" % (value, Cm2inch(value)))
        continue
    if menu == 4:
        print("%.2f 인치 ---> %.d센티미터" % (value, Inch2cm(value)))
        continue
    if menu == 5:
        print("%.2f 화씨온도 ---> %.2f 섭씨온도" % (value, TempF2C(value)))
        continue
    if menu == 6:
        print("%.2f섭씨 ---> %.2f화씨온도" % (value, TempC2F(value)))
        continue
    if menu == 7:
        break