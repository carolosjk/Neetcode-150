import sys
class Solution:

    def fib(self, n: int, cache: dict):
        if n <= 1:
            return n
        
        if n not in cache:
            cache[n] = self.fib(n-1,cache) + self.fib(n-2, cache)
        return cache[n]
        

    def climbStairs(self, n: int) -> int:
        cache = {0:1,1:1}        
        return self.fib(n+1,cache)

if __name__ == "__main__":
    solution = Solution()
    print(sys.getrecursionlimit())
    print(sys.setrecursionlimit(1000000))
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))
    print(solution.climbStairs(6))
    print(solution.climbStairs(30))
    print(solution.climbStairs(50))
    print(solution.climbStairs(70))
    print(solution.climbStairs(90))
    print(solution.climbStairs(500))
    print(solution.climbStairs(1000))
    print(solution.climbStairs(500000))


# 1 -> 1 (1)
# 2 -> 2 (1-1,2)
# 3 -> 3 (1-1-1, 1-2, 2-1)
# 4 -> 5 (1-1-1-1, 1-1-2, 1-2-1, 2-1-1, 2-2)
# 5 -> 8 (1-1-1-1-1, 1-1-1-2, 1-1-2-1, 1-2-1-1, 2-1-1-1, 1-2-2, 2-1-2, 2-2-1)
# 