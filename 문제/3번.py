myCafe = {
    '아메리카노': 2500,
    '아이스아메리카노': 3000,
    '카페라떼': 3500,
    '카푸치노': 3500,
    '카페모카': 4000
}
sum = 0
print("========== MENU ==========")
for key, value in myCafe.items():
    print(key, value)
print("==========================")
for key, value in myCafe.items():
    print(key, "주문량을 입력하세요 (잔):", end='')
    if key == "아메리카노":
        noA = int(input())
        sum += noA * value
    if key == "아이스아메리카노":
        noAA = int(input())
        sum += noAA * value
    if key == "카페라떼":
        noL = int(input())
        sum += noL * value
    if key == "카푸치노":
        noC = int(input())
        sum += noC * value
    if key == "카페모카":
        noM = int(input())
        sum += noM * value
print("주문하신 음료에 대한 결재금액은 ", sum, "원입니다.")
