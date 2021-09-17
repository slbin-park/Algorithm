from collections import defaultdict
from collections import deque

dq = deque()

n = int(input())
dic = defaultdict(list)
for i in range(n):
    a = input()
    b = a.split(' ')
    for i in range(1, 3):
        if b[i] != '.':
            try:
                dic[b[0]].append((b[i], i))
            except:
                dic[b[0]] = (b[i], i)


def dfs(a):  #1번
    print(a, end='')
    for i in dic[a]:
        dfs(i[0])


def dfs2(a):  #2번
    if len(dic[a]) > 0:
        if len(dic[a]) == 1 and dic[a][0][1] == 1:
            dfs2(dic[a][0][0])
            print(a, end='')
        elif len(dic[a]) == 1 and dic[a][0][1] == 2:
            print(a, end='')
            dfs2(dic[a][0][0])
        else:
            dfs2(dic[a][0][0])
            print(a, end='')
            dfs2(dic[a][1][0])
    else:
        print(a, end='')


def dfs3(a):  #2번
    if len(dic[a]) > 0:
        if len(dic[a]) == 1 and dic[a][0][1] == 1:
            dfs3(dic[a][0][0])
            print(a, end='')
        elif len(dic[a]) == 1 and dic[a][0][1] == 2:
            dfs3(dic[a][0][0])
            print(a, end='')
        else:
            dfs3(dic[a][0][0])
            dfs3(dic[a][1][0])
            print(a, end='')
    else:
        print(a, end='')


dfs('A')
print()
dfs2('A')
print()
dfs3('A')