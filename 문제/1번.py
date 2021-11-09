import sys

input = sys.stdin.readline

res = []
maxnum = 0
minnum = 100
while 1:
    print("점수를 입력하세요.(입력할 점수가 없다면 n을 입력하시오 : ", end="")
    n = input().strip()
    if n == 'n' or n == 'N':
        break
    elif n.isnumeric():
        if not 0 <= int(n) <= 100:
            print("입력이 잘못 되었습니다.")
        else:
            res.append(int(n))
            maxnum = max(int(n), maxnum)
            minnum = min(int(n), minnum)
    else:
        print("입력이 잘못 되었습니다.")
print("점수 리스트 : ", end="")
print(res)
print("최고 점수 : ", maxnum)
print("최저 점수 : ", minnum)
print("평   균 :", sum(res) / len(res))
