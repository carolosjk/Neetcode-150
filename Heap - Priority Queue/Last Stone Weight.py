from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            smallest = heapq.heappop(stones)
            sec_smallest = heapq.heappop(stones)

            new_stone = smallest - sec_smallest
            if new_stone < 0:
                heapq.heappush(stones,new_stone)
            

        
        return -stones[0] if stones else 0


    

if __name__ == "__main__":
    solution = Solution()
    print(solution.lastStoneWeight([2,3,6,2,4]))
    print(solution.lastStoneWeight([1,2]))
    print(solution.lastStoneWeight([]))
    print(solution.lastStoneWeight([3]))
    




