import time

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        cache = {}
        
        def dfs(d: int, buy: bool, sell: bool, hasCoin: bool) -> int:
            if d >= len(prices):
                return 0
            if (d,buy,sell,hasCoin) in cache:
                return cache[(d,buy,sell,hasCoin)]
            if buy:
                return -prices[d] + max( dfs(d+1,False,True,True), dfs(d+1,False,False,True) )
            elif sell:
                return prices[d] + max( dfs(d+2,True,False,False), dfs(d+2,False,False,False) )
            else:
                if hasCoin:
                    return max( dfs(d+1,False,True,True),dfs(d+1,False,False,True) )
                else:
                    return max( dfs(d+1,True,False,False),dfs(d+1,False,False,False) )
        
        return max(dfs(0,True,False,False),dfs(0,False,False,False))
            
            
    def maxProfit2(self, prices: list[int]) -> int:

        cache = {}

        def dfs(d:int, hasCoin: bool) -> int:
            if d >= len(prices):
                return 0
            if (d,hasCoin) in cache:
                return cache[(d,hasCoin)]
            do_nothing = dfs(d+1, hasCoin)
            if hasCoin:
                return max(do_nothing, prices[d]+dfs(d+2, False))
            else:
                return max(do_nothing, -prices[d]+dfs(d+1, True))
        return dfs(0,False)

        



        

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([1,3,4,0,4]))
    print(solution.maxProfit([]))
    print(solution.maxProfit([1]))
    print(solution.maxProfit([1,3]))
    print(solution.maxProfit([3,1]))
    print(solution.maxProfit2([48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]))



