import sys

input = sys.stdin.readline

n = input().strip()
a = n.split('*')
b = []  #찾는 문자열 들어있음
for i in range(len(a)):
    if a[i] != '':
        b.append(a[i])
blen = len(b)
m = int(input())
for i in range(m):
    ans = input().strip()
    index = 0
    if blen == 0:
        print(ans)
    else:
        for i in range(len(ans)):
            if ans[i] == b[index]:
                index += 1
            if index == blen:
                print(ans)
                break
