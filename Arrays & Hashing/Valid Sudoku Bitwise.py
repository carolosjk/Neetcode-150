from typing import List

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                number = int(board[r][c]) - 1

                if (1 << number) & rows[r]:
                    return False
                if (1 << number) & columns[c]:
                    return False
                if (1 << number) & boxes[(r//3)+(c//3)*3]:
                    return False
                
                rows[r] |= (1<<number)
                columns[c] |= (1<<number)
                boxes[(r//3)+(c//3)*3] |= (1<<number)

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
