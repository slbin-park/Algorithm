import sys
input = sys.stdin.readline #시작할때 해주면 좋음?
n = int(input())
arr = list()
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(n):
    print(arr[i])