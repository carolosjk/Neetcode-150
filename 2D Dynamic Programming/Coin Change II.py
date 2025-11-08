
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:

        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            for val in range(coin,amount+1):
                dp[val] += dp[val-coin]

        print(dp)
        
        return dp[amount]


        

if __name__ == "__main__":
    solution = Solution()
    print(solution.change(4, [1,2,3]))
    print(solution.change(9, [2,4]))
    print(solution.change(0, [2,4]))
