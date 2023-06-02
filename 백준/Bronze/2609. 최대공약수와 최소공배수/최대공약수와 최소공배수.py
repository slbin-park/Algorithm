from copy import deepcopy
import heapq
from collections import deque
from itertools import combinations
import sys


def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x
def LCM(x,y):
    return (x*y) // GCD(x,y)
input = sys.stdin.readline
n,m = map(int,input().split())
print(GCD(n,m))
print(LCM(n,m))
