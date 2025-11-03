from typing import List
import heapq

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def findComb(index: int, total: int, combo: List[int]):
            if total == target:
                combinations.append(combo.copy())
            elif total > target:
                return
            else:
                for i in range(index,len(nums)):
                    combo.append(nums[i])
                    findComb(i, total+nums[i], combo)
                    combo.pop()
        
        findComb(0, 0,[])

        return combinations

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2,5,6,9],9))
    print(sol.combinationSum([3,4,5],16))
    print(sol.combinationSum([3],5))