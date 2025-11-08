
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:

        rows = len(grid)
        cols = len(grid[0])
        positions = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:

                    search = deque()
                    search.append((i,j,0))

                    while search:
                        a,b,dis = search.popleft()

                        if grid[a][b] > 0:
                            grid[a][b] = min(grid[a][b],dis)

                        for x,y in positions:
                            if a+x >= 0 and a+x < rows and b+y >=0 and b+y < cols:
                                val = grid[a+x][b+y]
                                if val > dis+1:
                                    search.append((a+x,b+y,dis+1))

        print(grid)

if __name__ == "__main__":
    sol = Solution()
    sol.islandsAndTreasure([
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
        ])
