class Solution:

    def fib(self,n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def climbStairs(self, n: int) -> int:
        
        return self.fib(n+1)

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(1))
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))
    print(solution.climbStairs(6))


# 1 -> 1 (1)
# 2 -> 2 (1-1,2)
# 3 -> 3 (1-1-1, 1-2, 2-1)
# 4 -> 5 (1-1-1-1, 1-1-2, 1-2-1, 2-1-1, 2-2)
# 5 -> 8 (1-1-1-1-1, 1-1-1-2, 1-1-2-1, 1-2-1-1, 2-1-1-1, 1-2-2, 2-1-2, 2-2-1)
# 