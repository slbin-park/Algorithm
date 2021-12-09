import sys

input = sys.stdin.readline

heap = []

n, k = map(int, input().split())

arr = [0 for i in range(k)]
dia = [[0, 0] for i in range(n)]

for i in range(n):
    dia[i] = list(map(int, input().split()))
dia.sort(key=lambda x: (-x[1]))

for i in range(k):
    arr[i] = int(input())
arr.sort()

