class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i,row in enumerate(board):
            for j, tile in enumerate(row):
                if tile == ".":
                    continue
                else:
                    right = (row[j+1] == "X") if j+1 < len(row) else False
                    left = (row[j-1] == "X") if j-1 >= 0 else False
                    top = False
                    if i-1 >=0:
                        top = board[i-1][j] == "X"

                    
                    if not left:
                        if right:
                            count +=1
                        elif not top:
                            count += 1
            
        return count
                    