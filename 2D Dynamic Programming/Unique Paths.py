

class Solution:
    def calculatePaths(self, m, n, cm, cn, cache):
        if cm >= m or cn >= n:
            return 0
        
        if cm == (m-1) and cn == (n-1):
            return 1
        
        mn = str(cm) + "_" + str(cn)

        if mn in cache:
            return cache[mn]
        
        cache[mn] = self.calculatePaths(m,n,cm+1,cn,cache) + self.calculatePaths(m,n,cm,cn+1,cache)
        return cache[mn]

    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        return self.calculatePaths(m,n,0,0,cache)
        




        

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3,6))
    print(solution.uniquePaths(6,3))
    print(solution.uniquePaths(3,3))
    print(solution.uniquePaths(1,1))
