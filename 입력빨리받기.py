import sys
input = sys.stdin.readline #시작할때 해주면 좋음?
#한줄씩 받을때
m = int(input())

for i in range(m):
    a,b = map(int,input().split())
    print(a+b)