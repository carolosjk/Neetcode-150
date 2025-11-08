from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        islands = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1

                    search = deque()
                    search.append((i,j))
                    while search:
                        a,b = search.popleft()
                        if a-1 >= 0 and grid[a-1][b] == "1":
                            search.append((a-1,b))
                        if a+1 < n and grid[a+1][b] == "1":
                            search.append((a+1,b))
                        if b-1 >=0 and grid[a][b-1] == "1":
                            search.append((a,b-1))
                        if b+1 < m and grid[a][b+1] == "1":
                            search.append((a,b+1))
                        grid[a][b] = "0"                 
        
        return islands

    




if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands(
        [["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
    ))
    print(sol.numIslands(
        [["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
    ))