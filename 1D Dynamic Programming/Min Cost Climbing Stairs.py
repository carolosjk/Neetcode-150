from typing import List

class Solution:

    def calculateCost(self, cost: List[int], current: int, cache: List[int]) -> int:
        steps = len(cost)

        if current in cache:
            return cache[current]

        if steps <= current:
            return 0
        
        current_step_cost = cost[current]

        cache[current] = current_step_cost + min(self.calculateCost(cost,current+1, cache), self.calculateCost(cost,current+2, cache))
        return cache[current]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        return min(self.calculateCost(cost,0,cache), self.calculateCost(cost,1,cache))



        

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostClimbingStairs([1,2,3]))
    print(solution.minCostClimbingStairs([1,2,1,2,1,1,1]))
