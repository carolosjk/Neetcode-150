from typing import List
import heapq

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        nums.sort()

        def findCombo(index: int, sum: int, combo: List[int]) -> None:
            if sum == target:
                if not combo in combinations:
                    combinations.append(combo.copy())
            elif sum > target:
                return
            else:
                for i in range(index,len(nums)):
                    num = nums[i]
                    combo.append(num)
                    findCombo(i+1, sum+num, combo)
                    combo.pop()
        
        findCombo(0,0,[])        

        return combinations

if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([9,2,2,4,6,1,5],8))
    print(sol.combinationSum2([1,2,3,4,5],7))
    print(sol.combinationSum2([3],5))