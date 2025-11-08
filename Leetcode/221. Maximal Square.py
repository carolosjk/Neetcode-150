class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:

        if not matrix or len(matrix) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        dp = [[0]*m for _ in range(n)]
        max_height = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    continue
                left = top = diag = 0
                if i > 0: left = dp[i-1][j]
                if j > 0: top = dp[i][j-1]
                if j > 0 and i > 0: diag = dp[i-1][j-1]

                dp[i][j] = 1 + min(left,top,diag)
                max_height = max(max_height,dp[i][j])

        return max_height*max_height
        