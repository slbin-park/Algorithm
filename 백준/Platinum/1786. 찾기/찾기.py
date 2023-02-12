import sys
from collections import deque
import heapq

input = sys.stdin.readline


def make_table(pattern):
    table = [0 for _ in range(len(pattern))]
    i = 0
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    return table


def kmp(str1, pattern):
    table = make_table(pattern)
    result = []
    i = 0
    for j in range(len(str1)):
        while i > 0 and pattern[i] != str1[j]:
            i = table[i - 1]
        if pattern[i] == str1[j]:
            i += 1
            if i == len(pattern):
                result.append(j - len(pattern) + 2)
                i = table[i - 1]
    return result


str1 = input().rstrip()
pattern = input().rstrip()
result = kmp(str1, pattern)
print(len(result))
for i in result:
    print(i, end=" ")
