class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [-1] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for val in range(coin,amount+1):
                if val == coin:
                    dp[val] = 1
                elif dp[val-coin] != -1:
                    dp[val] = min(dp[val],dp[val-coin]+1) if dp[val] > 0 else dp[val-coin]+1

        return dp[amount]
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1,2,5],10))
    print(solution.coinChange([1,2,5],11))
    print(solution.coinChange([3,4],2))
    print(solution.coinChange([3,4],0))


#[1, 2, 5] -> 10
# [0,1,2,3,4,5,6,7,8,9,10]
# [0,1,1,2,2,3,3,4,4,5,5]
# [0,1,1,2,2,1,3,4,4,5,2]

#[2, 5] -> 10

# [0,0,0,0,0,0,0,0,0,0,0]
# [0,0,1,0,0,0,0,0,0,0,0]