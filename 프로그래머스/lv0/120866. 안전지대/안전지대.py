             
def solution(board):
    answer = 0
     
    n = len(board)
    print(n)
    def dfs(x,y) :
        dx = [0,0,1,-1,-1,-1,1,1]
        dy = [1,-1,0,0,-1,1,-1,1]
        for i in range(8) :
            nx = x+ dx[i]
            ny = y+ dy[i]
            if (0 <= nx < n) and (0 <= ny < n) :
                if board[nx][ny] == 0 :
                    board[nx][ny] = -1
                    
                    
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                dfs(i,j)
                
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 0 :
                answer+= 1
    return answer