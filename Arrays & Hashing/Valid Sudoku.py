from typing import List

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        columnDict = [{} for _ in range(9)]
        boxDict = [{} for _ in range(9)]

        for i,row in enumerate(board):
            rowDict = {}
            for j,num in enumerate(row):
                if num in rowDict:
                    return False
                if num in columnDict[j]:
                    return False
                
                boxIndex = (i//3)+(j//3)*3
                if num in boxDict[boxIndex]:
                    return False

                if num != ".":
                    rowDict[num] = True
                    columnDict[j][num] = True
                    boxDict[boxIndex][num] = True


        return True

    
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku(  [["1","2",".",".","3",".",".",".","."],
                                    ["4",".",".","5",".",".",".",".","."],
                                    [".","9","8",".",".",".",".",".","3"],
                                    ["5",".",".",".","6",".",".",".","4"],
                                    [".",".",".","8",".","3",".",".","5"],
                                    ["7",".",".",".","2",".",".",".","6"],
                                    [".",".",".",".",".",".","2",".","."],
                                    [".",".",".","4","1","9",".",".","8"],
                                    [".",".",".",".","8",".",".","7","9"]]))
    
    print(solution.isValidSudoku(  [["1","2",".",".","3",".",".",".","."],
                                    ["4",".",".","5",".",".",".",".","."],
                                    [".","9","1",".",".",".",".",".","3"],
                                    ["5",".",".",".","6",".",".",".","4"],
                                    [".",".",".","8",".","3",".",".","5"],
                                    ["7",".",".",".","2",".",".",".","6"],
                                    [".",".",".",".",".",".","2",".","."],
                                    [".",".",".","4","1","9",".",".","8"],
                                    [".",".",".",".","8",".",".","7","9"]]))


#   first we go through each row -> O(n^2)
#   for each one, we keep 3 dictionaries.
#   1. for each row
#   2. for each column
#   3. for each 3x3 box
#
#
#
#
#
#
