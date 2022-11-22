import sys
sys.setrecursionlimit(10**6)
def solution(word):
    answer = 0
    arr = ['A','E','I','O','U']
    words = []
    cword = []
    def dfs(index):
        if index == 5 and len(cword):
            words.append(''.join(cword))
            return
        for i in range(5):
            cword.append(arr[i])
            dfs(index+1)
            cword.pop()
    dfs(0)
    dfs(1)
    dfs(2)
    dfs(3)
    dfs(4)
    words.sort()
    for i in range(len(words)):
        if words[i] == word:
            answer = i+1
            break
    return answer