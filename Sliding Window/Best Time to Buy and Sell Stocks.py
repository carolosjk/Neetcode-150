from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuyPrice = float("inf")
        maxProfit = 0

        for price in prices:
            minBuyPrice = min(price,minBuyPrice)
            maxProfit = max(maxProfit,price-minBuyPrice)
        
        return maxProfit




if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([10,1,5,6,7,1]))
    print(solution.maxProfit([10,8,7,5,2]))