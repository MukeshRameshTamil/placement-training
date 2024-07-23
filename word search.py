class Solution(object):
    def exist(self, board, word):
    
        if len(word)>len(board)*len(board[0]):
            return False
        
        map = {}
        for i in word:
            map[i] = map.get(i,0)+1
        for i in board:
            for j in i:
                if j in map:
                    map[j] -= 1
        for i in map.values():
            if i>0:
                return False
        
        def dfs(i,j,k):
            if k == len(word):
                return True
            if i<0 or i>= len(board) or j<0 or j>= len(board[0]) or board[i][j] != word[k]:
                return False
            temp = board[i][j]
            board[i][j] = ''
            
            if dfs(i-1, j, k+1) or dfs(i+1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1):
                return True
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
