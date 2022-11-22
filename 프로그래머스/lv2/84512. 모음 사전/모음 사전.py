import sys
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
    for i in range(5):
        dfs(i)
    words.sort()
    for i in range(len(words)):
        if words[i] == word:
            answer = i+1
            break
    return answer