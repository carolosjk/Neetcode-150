
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        positions = [(0,1),(0,-1),(1,0),(-1,0)]
        remainingFruit = 0

        rotting = deque()
        reached = {}

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    remainingFruit +=1
                elif grid[i][j] == 2:
                    for x,y in positions:
                        if 0 <= i+x < rows and 0 <= j+y < cols:
                            if grid[i+x][j+y] == 1 and not (i+x,j+y) in reached:
                                rotting.append((i+x,j+y,1))
                                reached[(i+x,j+y)] = True


        while rotting:
            i,j,day = rotting.popleft()
            grid[i][j] = 2
            remainingFruit -= 1
            if remainingFruit == 0:
                return day
            
            for x,y in positions:
                if 0 <= i+x < rows and 0 <= j+y < cols:
                    if grid[i+x][j+y] == 1 and not (i+x,j+y) in reached:
                        rotting.append((i+x,j+y,day+1))
                        reached[(i+x,j+y)] = True

        return 0 if remainingFruit == 0 else -1



if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[1,1,0],[0,1,1],[0,1,2]]))
    print(sol.orangesRotting([[1,0,1],[0,2,0],[1,0,1]]))


    # [1,1,0]
    # [0,1,1]
    # [0,1,2]
